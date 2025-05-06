 import matplotlib.pyplot as plt
import seaborn as sns

def plot_score_distribution(df, column='score'):
    """Plot histogram of scores."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    
    sns.histplot(df[column], kde=True)
    plt.title("Distribution of Test Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
