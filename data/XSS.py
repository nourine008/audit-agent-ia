from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    #FAILLE : injection directe du input dans le HTML
    return f"<h1>Résultats pour : {query}</h1>"

# Attaque : ?q=<script>alert('XSS')</script>