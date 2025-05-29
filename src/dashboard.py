# src/dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

from src.load_data import load_test_results
from src.clean_data import clean_scores

# 1. Configuración de página
st.set_page_config(
    page_title="Interactive NYC Schools Dashboard",
    layout="wide"
)

# 2. Título
st.title("📊 NYC Public Schools Test Results Dashboard")

# 3. Carga y limpieza
df = load_test_results("data/test_results_2022.csv")
df = clean_scores(df)

# 4. Sidebar de filtros
boroughs = df['borough'].unique().tolist()
selected = st.sidebar.multiselect(
    "Select Boroughs", boroughs, default=boroughs
)
min_score = st.sidebar.slider("Minimum Score", 0, 100, 50)

# 5. Filtrado dinámico
df_filt = df[
    (df['borough'].isin(selected)) &
    (df['score'] >= min_score)
]

# 6. Métricas clave
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df_filt))
col2.metric("Average Score", round(df_filt['score'].mean(), 2))
col3.metric("Boroughs Selected", len(selected))

# 7. Gráfico de proporciones (pie)
st.subheader("Score Distribution by Borough")
fig1 = px.pie(
    df_filt.groupby('borough').size().reset_index(name='count'),
    names='borough', values='count',
    title="Proportion of Records"
)
st.plotly_chart(fig1, use_container_width=True)

# 8. Histograma interactivo
st.subheader("Score Histogram")
fig2 = px.histogram(
    df_filt, x='score', nbins=20,
    title="Score Frequency"
)
st.plotly_chart(fig2, use_container_width=True)

# 9. Mapa de ubicación aproximada
#    Si el CSV incluye lat/lon, úsalo; si no, generamos puntos ficticios
coords = {
    "Manhattan": (40.7831, -73.9712),
    "Brooklyn":  (40.6782, -73.9442),
    "Queens":    (40.7282, -73.7949),
    "Bronx":     (40.8448, -73.8648),
    "Staten Island": (40.5795, -74.1502)
}
df_map = df_filt.copy()
df_map['lat'] = df_map['borough'].map(lambda b: coords[b][0])
df_map['lon'] = df_map['borough'].map(lambda b: coords[b][1])

st.subheader("Geographic Distribution")
st.map(df_map[['lat', 'lon']])

# 10. Tabla de datos filtrados (opcional)
with st.expander("Show Filtered Data"):
    st.dataframe(df_filt.reset_index(drop=True))
