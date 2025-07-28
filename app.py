import streamlit as st
from pretraiteur import load_excel, compute_mttr, compute_mtta, compute_mttc
from generateur_de_graphiques import generate_chart

st.set_page_config(page_title="Analyse des KPIs - MTTR, MTTA, MTTC", layout="wide")
st.title("📊 Générateur de visualisation des KPIs à partir d’un fichier Excel")

uploaded_file = st.file_uploader(" Importer le fichier Excel", type=["xlsx"])

if uploaded_file:
    df = load_excel(uploaded_file)

    mttr_df = compute_mttr(df)
    mtta_df = compute_mtta(df)
    mttc_df = compute_mttc(df)

    st.success(" Fichier traité avec succès. Données calculées pour les 3 KPIs.")

    chart_type = st.selectbox(" Type de graphique :", ["Ligne", "Barres", "Pie", "Histogramme"])

    tabs = st.tabs([" MTTR", " MTTA", " MTTC"])

    with tabs[0]:
        st.subheader("Mean Time To Repair (MTTR)")
        st.dataframe(mttr_df)
        fig_mttr = generate_chart(mttr_df, "Month", "MTTR (h)", "Évolution mensuelle du MTTR", chart_type)
        st.plotly_chart(fig_mttr, use_container_width=True)

    with tabs[1]:
        st.subheader(" Mean Time To Acknowledge (MTTA)")
        st.dataframe(mtta_df)
        fig_mtta = generate_chart(mtta_df, "Month", "MTTA (h)", "Évolution mensuelle du MTTA", chart_type)
        st.plotly_chart(fig_mtta, use_container_width=True)

    with tabs[2]:
        st.subheader(" Mean Time To Close (MTTC)")
        st.dataframe(mttc_df)
        fig_mttc = generate_chart(mttc_df, "Month", "MTTC (h)", "Évolution mensuelle du MTTC", chart_type)
        st.plotly_chart(fig_mttc, use_container_width=True)
