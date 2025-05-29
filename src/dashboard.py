import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.visualize import (
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

data_path = "data/schools.csv"
df = load_data(data_path)

# 4. Sidebar filters
st.sidebar.header("Filters")
# Borough filter
boroughs = df["borough"].unique().tolist()
selected_boroughs = st.sidebar.multiselect(
    "Select Boroughs", boroughs, default=boroughs
)
# Metric filter
grid_cols = [c for c in df.columns if c.startswith("average_")] + ["percent_tested"]
selected_metric = st.sidebar.selectbox(
    "Choose Metric", grid_cols, index=0
)
# Minimum threshold slider
min_threshold = st.sidebar.slider(
    f"Minimum {selected_metric}",
    float(df[selected_metric].min()),
    float(df[selected_metric].max()),
    float(df[selected_metric].min())
)

# Apply dynamic filtering
df_filtered = df[
    (df["borough"].isin(selected_boroughs)) &
    (df[selected_metric] >= min_threshold)
]

# 5. Display key metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df_filtered))
col2.metric(
    f"Average {selected_metric}",
    round(df_filtered[selected_metric].mean(), 2) if len(df_filtered) else 0
)
col3.metric("Boroughs Selected", len(selected_boroughs))

# 6. Visualization Tabs
tabs = st.tabs(["Distribution", "Average by Borough", "Top Decile Schools"])

with tabs[0]:
    st.subheader("Score Distribution")
    fig, ax = plt.subplots()
    plot_score_distribution(df_filtered, column=selected_metric, ax=ax)
    st.pyplot(fig)

with tabs[1]:
    st.subheader("Average by Borough")
    fig, ax = plt.subplots()
    plot_average_by_borough(df_filtered, column=selected_metric, ax=ax)
    st.pyplot(fig)

with tabs[2]:
    st.subheader("Top Decile Schools")
    fig, ax = plt.subplots()
    plot_top_decile_schools(df_filtered, column=selected_metric, ax=ax)
    st.pyplot(fig)

# 7. Show raw data
with st.expander("Show Filtered Data"):
    st.dataframe(df_filtered.reset_index(drop=True))
