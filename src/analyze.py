def average_scores_by_borough(df):
    """Return the average score per borough."""
    if 'borough' not in df.columns or 'score' not in df.columns:
        raise ValueError("Missing required columns: 'borough' or 'score'")
    return df.groupby('borough')['score'].mean().sort_values(ascending=False)
