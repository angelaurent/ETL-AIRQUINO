# Conception d'un ETL

## Description

Ce projet vise à extraire, transformer et charger les données de qualité de l'air provenant de l'API AirQuino. Les données seront ensuite stockées dans une base de données MongoDB et visualisées à l'aide d'un tableau de bord Superset.

### Structure

le projet contient :

- 4 scripts python contenus dans le **dossier scripts**:
    1. **extract.py** qui contient une fonction python pour l'extraction
    2. **transform.py** qui contient une fonction python qui aggrege et calcule les moyennes des variables CO et PM2.5
    3. **load.py** qui contient une fonction qui permet la connexion entre mongo et python enfin y insere mes donnees.
    4. **etl.py** qui est mon fichier principal pour l'application des fonctions definies
- un dossier **IMAGE DASHBOARD** comprenant les images des dashboard de nos deux stations
- fichier **reponse aux questions** qui repond aux questions demandées dans le projet
- et un **README.md** qui contient la documentation du projet

## Table des matières

- [Description](#Description)
- [Structure ](#Structure)
- [Pré-requis](#Pré-requis)
- [Version](#Version)
- [Installation ](#Installation)
- [Usage](#Usage)
- [Demarrage](#Demarrage)
- [Documentation](#documentation)


### Pré-requis

- avoir un editeur de code comme vs code
- avoir python installé sur sa machine    _[Documentation](#documentation)_
- installer Mongodb sur sa machine local  _[Documentation](#documentation)_
- avoir docker installé sur sa machine    _[Documentation](#documentation)_
- avoir superset crées et en cours sur docker    _[Documentation](#documentation)_
- s'assurer d'avoir un serveur sql en cour sur sa machine et bien connectés à superset et mongodb.  _[Documentation](#documentation)_

### Version

- Mongodb compass = 1.40.4
- python = 3.10
- docker dekstop = 4.26.0

### Installation 
 cette partie concerne les installations des modules python utilisés pour mon projet

1. install pymongo

```bash
pip install pymongo
```
2. install pandas

```bash
pip install pandas
```

### Usage

```python
from pymongo import MongoClient
# pour ajouter un client 
client = MongoClient(mongo_host, mongo_port)

# pour inserer les données dans notre bd
collection.insert_many(data)
```

```python
import pandas as pd
# pour convertir notre contenu json en dataframe 
df = pd.DataFrame(data)

# pour convertir la colonne en datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])
```

### Demarrage

1. cloner le projet et l'enregistrer dans un dossier sur votre machine
2. ouvrir un terminal
3. se deplacer a la racine du projet enregistré sur votre machine
4. s'assurer d'etre dans scripts avant de lancer le projet
 ```bash
cd ETL/scripts
```
6. lancer "etl.py" et laisser la magie s'operer
```bash
 python etl.py
```
**(vous pouvez modifier vos acces de connexion a mongodb ainsi que l'URL de votre API selon vos besoins dans le fichier etl.py)**
7. pour plus de confirmation ouvrez mongodb et vous verrez vos base de donnees ainsi que vos collection.
8. ouvrez superset et amusez vous a creer votre dashboard avec les données obtenues. 

### Documentation

https://www.python.org/downloads/
https://superset.apache.org/docs/installation/installing-superset-using-docker-compose/
https://docs.docker.com/desktop/install/windows-install/
https://superset.apache.org/docs/creating-charts-dashboards/creating-your-first-dashboard
