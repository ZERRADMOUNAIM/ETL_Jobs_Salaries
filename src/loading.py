import sqlite3

def load_to_sqlite(df, db_name="data/processed/salaries.db"):
    # Création de la connexion à la base de données
    conn = sqlite3.connect(db_name)
    
    # Envoi du DataFrame vers une table SQL nommée 'salaries'
    # if_exists='replace' permet de repartir à zéro à chaque fois qu'on lance le pipeline
    df.to_sql('salaries', conn, if_exists='replace', index=False)
    
    conn.close()
    print(f"Données chargées avec succès dans {db_name} !")