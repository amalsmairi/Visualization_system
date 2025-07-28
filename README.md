#Développement d’un Systéme de visualisation automatique avec Streamlit et Plotly

Il s'agit d’un outil de lecture, traitement et visualisation de fichiers Excel contenant des données de tickets réseau, avec extraction automatique des indicateurs clés de performance (KPIs).

#Fonctionnalités principales:
-  Importation dynamique de fichiers Excel.
-  Nettoyage automatique des colonnes temporelles (`Created At`, `Updated At`, `complete_time`).
-  Calcul automatique des KPIs mensuels :
  - **MTTR** (Mean Time To Repair)
  - **MTTA** (Mean Time To Acknowledge)
  - **MTTC** (Mean Time To Close)
-  Génération de graphiques interactifs via Plotly :( Courbes (Line Chart)- Graphiques à barres (Bar Chart)- Camemberts (Pie Chart)- Histogrammes).
-  Interface web conviviale avec Streamlit
