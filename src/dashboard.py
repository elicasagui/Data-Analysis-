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

import streamlit as st as st
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

data_path = "data/schools.csv"  # use the actual CSV filename present in data/

