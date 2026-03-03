import os
import shutil
import kagglehub
import pandas as pd

def download_and_load_data():
    raw_dir = "data/raw"
    file_path = os.path.join(raw_dir, "ds_salaries.csv")
    
    # 1. Vérifier si la donnée est déjà là
    if not os.path.exists(file_path):
        print("Téléchargement des données depuis Kaggle...")
        os.makedirs(raw_dir, exist_ok=True)
        
        # Téléchargement via kagglehub
        download_path = kagglehub.dataset_download("saurabhshahane/data-science-jobs-salaries")
        
        # Trouver le fichier CSV dans le dossier téléchargé
        for file in os.listdir(download_path):
            if file.endswith(".csv"):
                shutil.copy(os.path.join(download_path, file), file_path)
        
        print(f"Données copiées dans : {file_path}")
    
    # 2. Chargement (Ingestion)
    df = pd.read_csv(file_path)
    return df