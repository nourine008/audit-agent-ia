#  Jeu de Test — Failles de Sécurité

## 1. SQL Injection — `sql_injection.py`
- **Ligne vulnérable :** concaténation directe du input dans la requête SQL
- **Attaque possible :** `' OR '1'='1` — récupère tous les utilisateurs
- **Ce que l'agent doit détecter :** absence de requêtes paramétrées

## 2. XSS — `xss.py`
- **Ligne vulnérable :** injection directe du input utilisateur dans le HTML
- **Attaque possible :** `?q=<script>alert('XSS')</script>`
- **Ce que l'agent doit détecter :** absence d'échappement du output HTML

## 3. Mots de passe en dur — `mots_de_passe_en_dur.py`
- **Ligne vulnérable :** credentials écrits en clair dans le code source
- **Attaque possible :** vol de credentials via accès au code (GitHub, etc.)
- **Ce que l'agent doit détecter :** hardcoded secrets (API keys, passwords, tokens)