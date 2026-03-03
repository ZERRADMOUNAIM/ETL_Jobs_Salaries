import pandas as pd

def clean_data(df):
    # 1. Mapping pour rendre les niveaux d'expérience plus clairs
    exp_mapping = {
        'EN': 'Entry-level',
        'MI': 'Mid-level',
        'SE': 'Senior-level',
        'EX': 'Executive-level'
    }
    df['experience_level'] = df['experience_level'].map(exp_mapping)
    
    # 2. On ne garde que les colonnes essentielles pour l'analyse
    columns_to_keep = [
        'work_year', 'experience_level', 'job_title', 
        'salary_in_usd', 'employee_residence', 'company_size'
    ]
    df_cleaned = df[columns_to_keep]
    
    # 3. Suppression des doublons potentiels
    df_cleaned = df_cleaned.drop_duplicates()
    
    return df_cleaned