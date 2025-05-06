def clean_scores(df):
    """
    Clean the test scores dataset.
    - Normalize column names
    - Drop rows with missing critical values
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    
    if 'score' in df.columns:
        df = df.dropna(subset=['score'])  # remove rows with no scores
        df['score'] = pd.to_numeric(df['score'], errors='coerce')
        df = df.dropna(subset=['score'])
    
    return df
