"""
fonction pour extraire mes données de l'API AIRQUINO
"""

import requests


def extract_donnee(api_url):
    """
    je recupere les donnees via l'url fourni grace a request
    et apres je lis les donnees recuperees qui precisons sont
    au format json
    """
    try:
        reponse = requests.get(api_url)  # recupere les donnees via l'API
        data = reponse.json().get("data")  # extraire les donnees json

        print("extraction reussie")
        return data

    except Exception:
        print('Erreur d\'extraction')
        return None
# fin #
