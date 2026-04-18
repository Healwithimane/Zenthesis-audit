import streamlit as st
import openai

# --- 1. CONFIGURATION DE L'INTERFACE (FRONT-END) ---
st.set_page_config(page_title="ZenThèse Domain Maturity", page_icon="🎯", layout="centered")

st.title("🎯 ZenThesis : Domain Maturity Audit")
st.write("Entrez vos variables de recherche pour diagnostiquer la maturité de votre sujet (Saturé, Émergent ou en Transition).")

# Les champs de saisie pour l'étudiant
concept_a = st.text_input("1. Concept A (Variable Indépendante)", placeholder="Ex: Algorithmes prédictifs")
concept_b = st.text_input("2. Concept B (Variable Dépendante / Livrable)", placeholder="Ex: Autonomie humaine")
contexte = st.text_input("3. Contexte (Environnement / Secteur)", placeholder="Ex: Industrie 5.0")

# --- 2. LE MOTEUR SECRET (BACK-END / PROPRIÉTÉ INTELLECTUELLE) ---
# L'étudiant ne verra jamais ce texte. C'est votre algorithme caché.
SYSTEM_PROMPT = """
<role>
You are the "ZenThesis Domain Maturity", an advanced academic engineering backend system designed to evaluate the maturity of a research domain.
</role>
<instructions>
The user will provide three inputs: Concept A, Concept B, and Context.
You must internally generate specific research queries, simulate the literature synthesis, and evaluate the semantic signals to determine if the research domain is Mature, New, or in Transition.
YOUR ENTIRE FINAL OUTPUT MUST BE EXCLUSIVELY IN ENGLISH, strictly following the tabular format and classification rules provided previously.
</instructions>
"""

# --- 3. L'EXÉCUTION ---
if st.button("Lancer l'Audit de Maturité 🚀"):
    if concept_a and concept_b and contexte:
        with st.spinner("Analyse sémantique de la littérature en cours... veuillez patienter."):
            
            try:
                # Connexion à l'API (nécessite votre clé secrète)
                openai.api_key = st.secrets["OPENAI_API_KEY"]
                
                # Assemblage des données de l'étudiant
                user_message = f"Concept A: {concept_a}\nConcept B: {concept_b}\nContext: {contexte}"

                # Envoi à l'IA
                response = openai.chat.completions.create(
                    model="gpt-4o", # Le modèle le plus performant
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_message}
                    ],
                    temperature=0.2 # Température basse pour un résultat académique strict
                )
                
                # Affichage du résultat généré par l'IA
                st.success("Audit terminé avec succès !")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Une erreur s'est produite lors de la connexion au moteur : {e}")
    else:
        st.warning("Veuillez remplir les 3 champs avant de lancer l'audit, Risk Commander.")
