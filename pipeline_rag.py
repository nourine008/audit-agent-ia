import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Configuration des dossiers
DATA_DIR = Path(r"C:\Users\Nouri\Desktop\audit-agent-ia\data")
VECTORSTORE_DIR = DATA_DIR / "vectorstore" / "faiss_index"

def traitement_des_documents():
    liste_morceaux_langchain = []
    
    # ---- PARTIE A : EXTRACTION DES PDF ET TXT (Texte classique) ----
    fichiers_pdf = list(DATA_DIR.glob("*.pdf"))
    fichiers_txt = list(DATA_DIR.glob("*.txt"))
    print(f"[*] Trouvé {len(fichiers_pdf)} fichiers PDF et {len(fichiers_txt)} fichiers .txt.")
    
    splitter_texte = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # Chargement PDF
    for chemin_pdf in fichiers_pdf:
        try:
            loader = PyPDFLoader(str(chemin_pdf))
            liste_morceaux_langchain.extend(splitter_texte.split_documents(loader.load()))
        except Exception as e:
            print(f"[!] Erreur PDF {chemin_pdf.name} : {e}")

    # Chargement TXT
    for chemin_txt in fichiers_txt:
        try:
            with open(chemin_txt, "r", encoding="utf-8", errors="ignore") as f:
                contenu = f.read()
                fragments = splitter_texte.split_text(contenu)
                for frag in fragments:
                    liste_morceaux_langchain.append(Document(page_content=frag, metadata={"source": chemin_txt.name}))
        except Exception as e:
            print(f"[!] Erreur TXT {chemin_txt.name} : {e}")

    # ---- PARTIE B : PARSING LOGIQUE DU CODE SOURCE (LanguageParser) ----
    print("[*] Analyse logique des fichiers de code via LanguageParser...")
    
    # 🔧 CORRECTION ICI : Remplacement de from_path par from_filesystem
    loader_code = GenericLoader.from_filesystem(
        path=str(DATA_DIR),
        glob="*.py",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=10)
    )
    
    try:
        documents_code = loader_code.load()
        # On découpe ensuite le code en conservant la cohérence syntaxique
        splitter_code = RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON,
            chunk_size=1000,
            chunk_overlap=100
        )
        fragments_code = splitter_code.split_documents(documents_code)
        liste_morceaux_langchain.extend(fragments_code)
        print(f"[+] {len(fragments_code)} morceaux de code logique ajoutés.")
    except Exception as e:
        print(f"[!] Erreur lors du parsing du code : {e}")
            
    return liste_morceaux_langchain

# ---- PARTIE C : MISE À ZONE DE LA BASE FAISS ----
if __name__ == "__main__":
    print("=== RUN : PIPELINE AVEC LANGUAGE PARSER ===")
    
    tous_nos_morceaux = traitement_des_documents()
    
    if tous_nos_morceaux:
        print(f"[+] Total général : {len(tous_nos_morceaux)} fragments prêts.")
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        print("[*] Calcul des vecteurs et mise à jour de FAISS...")
        base_vectorielle = FAISS.from_documents(tous_nos_morceaux, embeddings)
        base_vectorielle.save_local(str(VECTORSTORE_DIR))
        print("=== COMPILATION TERMINÉE ET CHARGÉE EN LOCAL ! ===")
    else:
        print("[!] Erreur : Aucun document extrait.")