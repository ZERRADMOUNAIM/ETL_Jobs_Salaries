
# 📊 End-to-End Data Engineering Pipeline: DS Salaries Analysis

## 📝 Présentation du Projet

Ce projet est un pipeline ETL (Extract, Transform, Load) complet conçu pour analyser les salaires dans le domaine de la Data Science. L'objectif est de transformer des données brutes issues de Kaggle en un dashboard BI interactif et exploitable.

## 🏗️ Architecture du Projet

Le projet suit une structure modulaire pour garantir la maintenabilité et la séparation des responsabilités :

- **Extraction** : Ingestion automatisée des données via l'API Kaggle.
- **Transformation** : Nettoyage, normalisation des niveaux d'expérience et filtrage avec Pandas.
- **Stockage** : Chargement des données structurées dans une base de données SQL (SQLite).
- **Visualisation** : Interface BI interactive construite avec Streamlit et Plotly.

## 📁 Structure du Repository

```text
ETL_Jobs/
├── data/
│   ├── raw/            # Données brutes (CSV)
│   └── processed/      # Base de données SQLite (.db)
├── src/
│   ├── extraction.py   # Script de téléchargement
│   ├── transformation.py # Logique de nettoyage
│   └── loading.py      # Chargement vers SQL
├── main.py             # Point d'entrée du pipeline
├── app.py              # Dashboard Streamlit
└── requirements.txt    # Dépendances du projet
```


## 🛠️ Technologies Utilisées

* **Python 3.x**
* **Pandas** : Manipulation et nettoyage de données.
* **SQLite** : Moteur de base de données relationnelle.
* **Streamlit** : Création du dashboard interactif.
* **Kagglehub** : Automatisation de la récupération des datasets.



## Installation et Utilisation

1. **Cloner le projet** :

   ```
   git clone [https://github.com/ton-pseudo/ETL_Jobs.git](https://github.com/ton-pseudo/ETL_Jobs.git)
   cd ETL_Jobs
   ```
2. **Installer les dépendances** :

   ```
   pip install -r requirements.txt
   ```
3. **Lancer le pipeline ETL** (Extraction -> SQL) :

   ```
   python main.py
   ```
4. **Lancer le Dashboard** :

   ```
   streamlit run app.py
   ```
