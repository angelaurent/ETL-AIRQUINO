"""
fonction load qui chargera mes donnees dans des bd mongo
"""

from pymongo import MongoClient


def load_to_mongo(data, mongo_host, mongo_port, database, collection):
    """
    je cree un client mongo en precisant le port et le host pour faciliter la
    connexion a mongo , de meme je precise le nom de ma base de données et de
    ma collection a creer et enfin j'insere mes données dans la bd crée.
    """

    client = MongoClient(mongo_host, mongo_port)
    db = client[database]
    collection = db[collection]

    try:
        # conversion car mongo ne reconnait pas le type date
        data['date'] = data['date'].astype(str)
        # conversion en dictionnaire pour inserer dans mongo
        data = data.to_dict(orient='records')
        # insertion dans ma bd
        collection.insert_many(data)
        print('bravo,vos données sont bien stockée')

    except Exception:
        print("desole l'insertion n'a pas ete effective")

    finally:
        client.close()

# fin de ma fonction #
