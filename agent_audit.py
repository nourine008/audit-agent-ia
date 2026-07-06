import os
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent

# 1. Configuration de la clé API Groq
os.environ["GROQ_API_KEY"] = "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"

print("[*] Connexion au modèle Llama-4-Scout...")
# 2. Configuration du modèle Llama-4-Scout
llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0  # Mode strict pour l'audit de sécurité
)

print("[*] Connexion à la base vectorielle FAISS...")
# 3. Chargement de la base vectorielle FAISS construite en Semaine 2
VECTORSTORE_DIR = r"C:\Users\Nouri\Desktop\audit-agent-ia\data\vectorstore\faiss_index"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
base_vectorielle = FAISS.load_local(VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)

# 4. Définition de l'Outil (Tool) pour l'Agent
@tool
def chercher_regles_securite(query: str) -> str:
    """Utile pour chercher des fiches OWASP et des documentations de vulnérabilités sur une faille précise."""
    docs = base_vectorielle.similarity_search(query, k=2)
    return "\n---\n".join([d.page_content for d in docs])

tools = [chercher_regles_securite]
print("[+] Étape 3.2 Réussie : L'outil de recherche RAG est prêt et lié à FAISS !")

# 5. Le Prompt ReAct (Le protocole exigé par le BRD)
template = """Tu es un auditeur de sécurité expert et rigoureux. Ton rôle est d'analyser le code Python fourni par l'utilisateur pour y détecter des vulnérabilités (ex: SQL Injection, XSS, Secrets en dur) en te basant exclusivement sur les standards de sécurité issus de tes outils.

Pour chaque vulnérabilité détectée, tu dois impérativement formater ta réponse finale selon cette structure exacte (ne change aucun mot) :
- **Ligne du code problématique** : [Numéro ou extrait de la ligne]
- **Nom de la faille** : [Nom précis de la faille]
- **Explication du risque** : [Pourquoi c'est dangereux et l'impact]
- **Code corrigé** : [Bloc de code propre et sécurisé]

Tu as accès aux outils suivants :
{tools}

Pour résoudre la tâche, utilise scrupuleusement le format de pensée suivant :
Thought: Tu devez toujours réfléchir à ce que tu cherches (ex: analyser si une ligne est vulnérable).
Action: L'action à entreprendre, doit être l'une de ces valeurs : {tool_names}
Action Input: L'argument précis à envoyer à l'outil (ex: "SQL Injection mitigation")
Observation: Le résultat renvoyé par l'outil.
... (cette étape Thought/Action/Action Input/Observation peut se répéter si nécessaire)
Thought: Je connais maintenant la réponse finale basée sur les faits.
Final Answer: [Ton rapport d'audit structuré final ici, en respectant les 4 puces obligatoires]

Code à auditer :
{input}

Thought: {agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)
print("[+] Étape 3.3 Réussie : Le prompt ReAct conforme au BRD est configuré !")

# 6. Assemblage logique de l'Agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,                # Affiche le raisonnement (Thought) en temps réel
    handle_parsing_errors=True   # Évite les crashs de format
)

if __name__ == "__main__":
    chemin_script_test = r"C:\Users\Nouri\Desktop\audit-agent-ia\__les_failles__\sql_injection.py"
    
    print("\n==================================================")
    print("[*] OUVERTURE ET ANALYSE DU FICHIER VULNÉRABLE...")
    print("==================================================")
    
    if os.path.exists(chemin_script_test):
        with open(chemin_script_test, "r", encoding="utf-8") as f:
            code_a_auditer = f.read()
        
        print("[*] Lancement de l'Agent IA (Llama-4-Scout)... Veuillez patienter.\n")
        resultat = agent_executor.invoke({"input": code_a_auditer})
        
        print("\n==================================================")
        print("  RAPPORT D'AUDIT SÉCURITÉ FINAL (CONFORME AU BRD) :")
        print("==================================================")
        print(resultat["output"])
    else:
        print(f"[!] Erreur : Le fichier de test n'existe pas au chemin : {chemin_script_test}")