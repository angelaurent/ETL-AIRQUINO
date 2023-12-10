"""
ce script me permet d'executer mes fonctions etl definis dans les autres
fichiers
"""
from extract import extract_donnee
# import extract
import transform
import load

# STATION 1 #
print("################### DEBUT DE LA STATION 1 ########################")
# ACCES DE LA STATION 1 #
STATION1_URL = 'https://airqino-api.magentalab.it/v3/getStationHourlyAvg/\
283164601'
MONGO_HOST = 'localhost'
MONGO_PORT = 27018
DATABASE = 'data_station1'
COLLECTION = 'station1'
# appliquons mes fonctions
don = extract_donnee(STATION1_URL)
dat = transform.transform(don)
load.load_to_mongo(dat, MONGO_HOST, MONGO_PORT, DATABASE, COLLECTION)
print("################ FIN STATION 1 #############################")


# STATION 2 #
print("################### DEBUT DE LA STATION 2 ########################")
# ACCES DE LA STATION 2 #
STATION2_URL = 'https://airqino-api.magentalab.it/v3/getStationHourlyAvg/\
283181971'
MONGO_HOST = 'localhost'
MONGO_PORT = 27018
DATABASE = 'data_station2'
COLLECTION = 'station2'
# appliquons mes fonctions
don = extract_donnee(STATION2_URL)
dat = transform.transform(don)
load.load_to_mongo(dat, MONGO_HOST, MONGO_PORT, DATABASE, COLLECTION)
print("#################### FIN DES INSERTIONS #######################")
