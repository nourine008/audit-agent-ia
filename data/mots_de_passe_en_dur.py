
import requests

#  FAILLE : credentials hardcodés en clair
API_KEY = "sk-prod-12345SECRET"
DB_PASSWORD = "admin123"
SECRET_TOKEN = "super_secret_jwt_token"

def connect_to_api():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    return requests.get("https://api.example.com/data", headers=headers)