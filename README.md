#  Audit Agent IA — Auditeur de Code Basé sur RAG

> Un agent IA spécialisé qui transforme un LLM généraliste en véritable auditeur de sécurité, capable d'analyser du code source et de détecter les vulnérabilités OWASP Top 10 en s'appuyant sur une base de connaissances vectorielle (RAG) plutôt que sur ses seules connaissances internes.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG%20%2B%20Agent-green)
![FAISS](https://img.shields.io/badge/VectorStore-FAISS-orange)
![LLM](https://img.shields.io/badge/LLM-Groq%20%2F%20LLaMA%203-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

##  Sommaire

- [Vision du projet](#-vision-du-projet)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture](#-architecture)
- [Stack technique](#-stack-technique)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Exemple de résultat](#-exemple-de-résultat)
- [Jeu de test](#-jeu-de-test)
- [Tests End-to-End](#-tests-end-to-end)
- [Limites connues](#-limites-connues)
- [Roadmap](#-roadmap)


---

##  Vision du projet

L'objectif de ce projet est de transformer un LLM classique en un **auditeur de code spécialisé**, fiable et traçable. Contrairement à un chatbot généraliste qui peut halluciner des vulnérabilités inexistantes ou passer à côté de failles réelles, cet agent **ancre chaque diagnostic dans une documentation de sécurité vérifiée** (OWASP Top 10, rapports CVE, bonnes pratiques).

Deux défis techniques structurent le projet :

1. **Construire une base vectorielle riche et pertinente** en matière de sécurité, pour minimiser les hallucinations du LLM.
2. **Apprendre à l'IA à raisonner sur la structure d'un code source** (fonctions, classes, blocs logiques) plutôt que de le traiter comme du texte conversationnel découpé arbitrairement.

---

##  Fonctionnalités

-  **Détection automatique des vulnérabilités OWASP Top 10** (injection SQL, XSS, credentials en dur, etc.)
-  **RAG (Retrieval-Augmented Generation)** : chaque réponse de l'agent s'appuie sur des extraits réels de documentation OWASP/CVE, pas sur la mémoire du LLM
-  **Parsing intelligent du code** : découpage par fonction/classe grâce au `LanguageParser` de LangChain (pas de découpage par paragraphe)
-  **Agent ReAct (Reason + Act)** : l'agent raisonne, interroge la base vectorielle, puis agit en formulant un diagnostic structuré
-  **Réponses structurées** selon un format fixe :
  ```
  Ligne de code posant problème → Nom de la faille → Explication → Code corrigé
  ```
-  **Interface web simple** pour uploader un fichier `.py` ou `.js` et visualiser l'audit en temps réel
-  **Inférence rapide** via l'API Groq (LLaMA 3)

---

##  Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        UTILISATEUR                                │
│              (upload fichier .py / .js via interface web)         │
└───────────────────────────────┬───────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PARSING DU CODE SOURCE                         │
│        LangChain LanguageParser → découpage par fonction/classe   │
└───────────────────────────────┬───────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                     AGENT IA (ReAct Pattern)                      │
│   Reason → identifie les patterns suspects dans le code           │
│   Act    → interroge la base vectorielle FAISS                    │
└───────────────────────────────┬───────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│              BASE VECTORIELLE (FAISS + HuggingFace Embeddings)    │
│   Documentation OWASP Top 10 · Rapports CVE · Bonnes pratiques    │
└───────────────────────────────┬───────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LLM — Groq API (LLaMA 3)                        │
│   Génère le diagnostic final basé UNIQUEMENT sur le contexte RAG  │
└───────────────────────────────┬───────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                  RÉPONSE STRUCTURÉE À L'UTILISATEUR                │
│     Faille détectée → Explication du risque → Correctif proposé    │
└─────────────────────────────────────────────────────────────────┘
```

---

##  Stack technique

| Composant | Technologie |
|---|---|
| Langage | Python 3.11 |
| Orchestration Agent | LangChain / LangGraph |
| Base vectorielle | FAISS |
| Embeddings | HuggingFace Embeddings |
| LLM | Groq API (LLaMA 3) |
| Parsing de code | LangChain `LanguageParser` |
| Pattern d'agent | ReAct (Reason + Act) |
| Frontend | Interface web (upload + affichage temps réel) |
| Source de connaissances | OWASP Top 10, rapports CVE, guides de bonnes pratiques |

---

##  Installation

### Prérequis

- Python 3.10 ou 3.11 ( Python 3.14 non compatible avec PyTorch au moment de l'écriture)
- Une clé API Groq ([console.groq.com](https://console.groq.com))

### Étapes

```bash
# 1. Cloner le repo
git clone https://github.com/<votre-username>/audit-agent-ia.git
cd audit-agent-ia

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Ajouter votre GROQ_API_KEY dans le fichier .env
```

### Exemple de `.env`

```env
GROQ_API_KEY=votre_clé_api_ici
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
VECTORSTORE_PATH=./data/faiss_index
```

---

## Utilisation

### 1. Construire la base vectorielle (une seule fois)

```bash
python pipeline_rag.py
```
Ce script télécharge/charge la documentation OWASP et CVE, la découpe en chunks, génère les embeddings (HuggingFace) et les stocke dans l'index FAISS (`data/`).

### 2. Tester la recherche par similarité (optionnel)

```bash
python interroger_rag.py
```
Permet de vérifier que la base vectorielle renvoie bien les bons extraits de documentation pour une requête donnée (ex: "Injection SQL").

### 3. Lancer l'audit sur un fichier de code

```bash
python agent_audit.py --file __les_failles__/sql_injection.py
```

### 4. Lancer l'interface web

```bash
python app.py
```
Puis ouvrir [http://localhost:8501](http://localhost:8501) et uploader un fichier `.py` ou `.js` pour lancer l'audit en temps réel.

---

##  Structure du projet

```
audit-agent-ia/
├── __les_failles__/           # Jeu de test : scripts contenant des failles intentionnelles
│   ├── mots_de_passe_en_dur.py
│   ├── sql_injection.py
│   └── XSS.py
├── BRD && PROJECT_CARD/        # Documentation projet (Cahier des Charges, Project Card)
├── data/                       # Documentation OWASP/CVE + index vectoriel FAISS
├── venv/                       # Environnement virtuel Python
├── pipeline_rag.py             # Construction de la base vectorielle (ingestion + embeddings)
├── interroger_rag.py           # Recherche par similarité dans la base FAISS
├── agent_audit.py              # Logique de l'agent (ReAct, prompts, orchestration)
├── app.py                      # Point d'entrée : interface web
├── requirements.txt
└── README.md
```

---

##  Exemple de résultat

**Fichier audité :** `login.py`

```python
query = "SELECT * FROM users WHERE username = '" + username + "'"
```

**Sortie de l'agent :**

```
 Ligne détectée : query = "SELECT * FROM users WHERE username = '" + username + "'"

Faille : Injection SQL (OWASP A03:2021 – Injection)

Explication : La concaténation directe de l'entrée utilisateur dans la requête SQL
permet à un attaquant d'injecter des instructions SQL arbitraires (ex: ' OR '1'='1),
contournant l'authentification ou exposant la base de données.

 Code corrigé :
query = "SELECT * FROM users WHERE username = %s"
cursor.execute(query, (username,))
```

---

##  Jeu de test

Le dossier `__les_failles__/` contient des scripts Python avec des failles **intentionnelles**, utilisés pour valider la détection de l'agent :

| Script | Faille testée |
|---|---|
| `sql_injection.py` | Injection SQL |
| `XSS.py` | Cross-Site Scripting (XSS) |
| `mots_de_passe_en_dur.py` | Identifiants / mots de passe codés en dur |

---

##  Tests End-to-End

Les tests E2E consistent à faire passer chaque script du dossier `__les_failles__/` dans `agent_audit.py` et à vérifier que :
- L'agent détecte **toutes** les failles connues du jeu de test
- L'agent ne génère **pas de faux positifs** sur du code sain
- Les réponses respectent bien le format structuré attendu (Ligne → Faille → Explication → Correctif)

---

##  Limites connues

- L'agent se limite aux vulnérabilités couvertes par la base documentaire ingérée (OWASP Top 10 + CVE sélectionnés)
- Les langages supportés pour le parsing structurel sont actuellement **Python** et **JavaScript**
- Les performances de détection dépendent de la qualité et de la couverture du corpus RAG

---

## Roadmap

- [ ] Support de langages additionnels (Java, PHP)
- [ ] Ajout d'un scoring de sévérité (CVSS) par faille détectée
- [ ] Génération automatique de rapports PDF exportables
- [ ] Intégration CI/CD (audit automatique sur chaque pull request)
