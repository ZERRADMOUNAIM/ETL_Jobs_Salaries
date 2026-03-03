import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px # Une super bibliothèque pour des graphiques pro

# --- Configuration et Données ---
st.set_page_config(page_title="Data Salary BI", layout="wide")

def get_data():
    conn = sqlite3.connect('data/processed/salaries.db')
    df = pd.read_sql("SELECT * FROM salaries", conn)
    conn.close()
    return df

df = get_data()

# --- Barre Latérale (Filtres) ---
st.sidebar.header("Filtres")
# On laisse l'utilisateur choisir les niveaux d'expérience
niveaux = st.sidebar.multiselect(
    "Niveau d'expérience :",
    options=df['experience_level'].unique(),
    default=df['experience_level'].unique()
)

# Filtrage du DataFrame
mask = df['experience_level'].isin(niveaux)
df_filtered = df[mask]

# --- Visualisation ---
st.title("📊 Dashboard BI : Salaires Data Science")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Salaire moyen par Métier")
    # On calcule la moyenne par métier
    avg_salary = df_filtered.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).reset_index()
    
    # Un graphique interactif avec Plotly
    fig = px.bar(avg_salary, x='salary_in_usd', y='job_title', orientation='h',
                 labels={'salary_in_usd': 'Salaire (USD)', 'job_title': 'Métier'})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Répartition par Taille d'Entreprise")
    fig2 = px.pie(df_filtered, names='company_size', values='salary_in_usd', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)