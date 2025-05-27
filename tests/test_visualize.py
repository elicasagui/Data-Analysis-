# tests/test_visualize.py

import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src.visualize import plot_score_distribution

def test_plot_score_distribution_creates_figure():
    df = pd.DataFrame({'score': [1, 2, 3, 4]})
    # Debe ejecutarse sin excepción y generar al menos una figura
    before = set(plt.get_fignums())
    plot_score_distribution(df, column='score')
    after = set(plt.get_fignums())
    assert len(after - before) == 1

def test_plot_score_distribution_missing_column():
    df = pd.DataFrame({'other': [1, 2]})
    with pytest.raises(ValueError):
        plot_score_distribution(df, column='score')
