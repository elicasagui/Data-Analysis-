# src/dashboard.py

import os
import sys

# Add project root and src folder to sys.path for module resolution
current_file = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(os.path.dirname(current_file), os.pardir))
src_path = os.path.join(project_root, "src")
for path in (project_root, src_path):
    if path not in sys.path:
        sys.path.insert(0, path)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from visualize import (
    plot_score_distribution,
    plot_average_by_borough,
    plot_top_decile_schools
)

# 1. Page configuration
st.set_page_config(
    page_title="Interactive NYC Schools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Title
st.title("📊 NYC Public Schools Test Results Dashboard")

# 3. Data loading
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

# Ensure correct path to data file
data_path = os.path.join(project_root, "data", "schools.csv")

df = load_data(data_path)

# 4. Sidebar filters
st.sidebar.header("Filters")
boroughs = df.get("borough", []).unique().tolist()
selected_boroughs = st.sidebar.multiselect(
    "Select Boroughs", boroughs, default=boroughs
)
# Metrics: any column starting with 'average_' or 'percent_tested'
metrics = [col for col in df.columns if col.startswith("average_")] + ["percent_tested"]
selected_metric = st.sidebar.selectbox(
    "Choose Metric", metrics, index=0
)
min_threshold = st.sidebar.slider(
    f"Minimum {selected_metric}",
    float(df[selected_metric].min()),
    float(df[selected_metric].max()),
    float(df[selected_metric].min())
)

# 5. Apply filters
df_filtered = df[
    (df["borough"].isin(selected_boroughs)) &
    (df[selected_metric] >= min_threshold)
]

# 6. Display key metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df_filtered))
col2.metric(
    f"Average {selected_metric}",
    round(df_filtered[selected_metric].mean(), 2) if not df_filtered.empty else 0
)
col3.metric("Boroughs Selected", len(selected_boroughs))

# 7. Visualization tabs
tab1, tab2, tab3 = st.tabs([
    "Distribution", "Average by Borough", "Top Decile Schools"
])

with tab1:
    st.subheader("Score Distribution")
    fig, ax = plt.subplots()
    plot_score_distribution(df_filtered, column=selected_metric, ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader("Average by Borough")
    fig, ax = plt.subplots()
    plot_average_by_borough(df_filtered, column=selected_metric, ax=ax)
    st.pyplot(fig)

with tab3:
    st.subheader("Top Decile Schools")
    fig, ax = plt.subplots()
    plot_top_decile_schools(df_filtered, column=selected_metric, ax=ax)
    st.pyplot(fig)

# 8. Show raw data
with st.expander("Show Filtered Data"):
    st.dataframe(df_filtered.reset_index(drop=True))
