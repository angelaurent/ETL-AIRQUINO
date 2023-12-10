"""
fonction transform qui calculera les moyennes.
"""

import pandas as pd


def transform(data):
    """
    cette fonction convertit mes donnees au format json en dataframe puis
    convertis la colonne timestamp en datetime et extrait la date unqiuement
    pour la sauvegarder dans une nouvelle colonne et enfin aggrege mes données
    selon la date et calcul la moyenne des colonnes CO et PM2.5
    """
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    df = df.groupby('date').agg({"CO": "mean", "PM2.5": "mean"}).reset_index()
    print("transformation effectuée avec succes")
    return df

# fin #
