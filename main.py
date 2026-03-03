from src.extraction import download_and_load_data
from src.transformation import clean_data
from src.loading import load_to_sqlite

def main():
    print("--- Début du Pipeline ---")
    
    # Appel de la fonction d'extraction
    df = download_and_load_data()
    
    if df is not None:
        print(f"Succès ! {len(df)} lignes ont été chargées.")
        print(df.head())

        # Appel de la fonction de transformation
        df_cleaned = clean_data(df)

        # Loading de la data
        load_to_sqlite(df, db_name="data/processed/salaries.db")
    else:
        print("Erreur : Le DataFrame est vide.")



if __name__ == "__main__":
    main()