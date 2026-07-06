from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Chemins vers ta base FAISS locale
DATA_DIR = Path(r"C:\Users\Nouri\Desktop\audit-agent-ia\data")
VECTORSTORE_DIR = DATA_DIR / "vectorstore" / "faiss_index"

print("[*] Chargement du modèle de vecteurs...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("[*] Connexion à la base de connaissances FAISS...")
base_vectorielle = FAISS.load_local(
    str(VECTORSTORE_DIR), 
    embeddings, 
    allow_dangerous_deserialization=True
)
print("[+] Base chargée avec succès !\n")
# POSE TA QUESTION ICI
question = "c'est quoi le xss"
print(f" Question : '{question}'")
print("[*] Recherche des extraits les plus pertinents...")

# Recherche des 3 meilleurs morceaux de texte
resultats = base_vectorielle.similarity_search(question, k=3)

print("\n================ EXTRAITS TROUVÉS INSTRUCTIONS ================")
for i, doc in enumerate(resultats, 1):
    print(f"\n [Source {i}] Fichier : {doc.metadata.get('source', 'Inconnu')}")
    print(f"Contenu :\n{doc.page_content}")
    print("-" * 60)