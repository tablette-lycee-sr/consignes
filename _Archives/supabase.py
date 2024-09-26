import requests
import json

# Remplacez ces valeurs par celles de votre projet Supabase
url = "https://tdvmzdamxekmmsxbnshp.supabase.co/rest/v1/snt"  # URL de votre table "utilisateurs"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRkdm16ZGFteGVrbW1zeGJuc2hwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjczNzU0NDgsImV4cCI6MjA0Mjk1MTQ0OH0.OxkfIeL36iXLN-nSaMy2CuHrcpBKIqMvanNeYxW1YvY"  # Remplacez par la clé d'API anonyme





# En-têtes pour l'API
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Fonction pour poster des données
def poster_donnees(Argt_nom, Argt_Activite_01_1):
    data = {
        "nom": Argt_nom,
        "Activite_01_1": Argt_Activite_01_1
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print(f"Données ajoutées : {nom}, {Activite_01_1}")
    else:
        print("Erreur lors de l'ajout des données :", response.json())

# Fonction pour lire des données
def lire_donnees():
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        utilisateurs = response.json()
        for utilisateur in utilisateurs:
            print(utilisateur)
    else:
        print("Erreur lors de la lecture des données :", response.json())

# Exemple d'utilisation
poster_donnees("Alice", 1)
poster_donnees("Bob", 1)
lire_donnees()
