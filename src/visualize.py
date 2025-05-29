# src/visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_score_distribution(df, column='score', ax=None):
    """Plot histogram of scores with KDE."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    if ax is None:
        _, ax = plt.subplots()
    sns.histplot(df[column].dropna(), kde=True, ax=ax)
    ax.set_title("Distribution of Test Scores")
    ax.set_xlabel("Score")
    ax.set_ylabel("Frequency")
    ax.grid(True)
    plt.tight_layout()


def plot_average_by_borough(df, column='score', ax=None):
    """Plot average score by borough as bar chart."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    grouped = df.groupby('borough')[column].mean().sort_values(ascending=False)
    if ax is None:
        _, ax = plt.subplots()
    grouped.plot(kind='bar', ax=ax)
    ax.set_title(f"Average {column} by Borough")
    ax.set_xlabel("Borough")
    ax.set_ylabel(f"Average {column}")
    ax.grid(axis='y')
    plt.tight_layout()


def plot_top_decile_schools(df, column='score', ax=None, top_percent=10):
    """Plot top decile of schools by score as horizontal bar chart."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    # Calcular umbral de percentil
    threshold = np.nanpercentile(df[column], 100 - top_percent)
    top_df = df[df[column] >= threshold].copy()
    if 'school_name' not in top_df.columns:
        raise ValueError("Column 'school_name' not found in DataFrame.")
    top_df = top_df.sort_values(column, ascending=True).tail(10)
    if ax is None:
        _, ax = plt.subplots()
    sns.barplot(x=column, y='school_name', data=top_df, ax=ax)
    ax.set_title(f"Top {top_percent}% Schools by {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("School Name")
    plt.tight_layout()
