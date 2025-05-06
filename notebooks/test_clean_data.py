import pandas as pd
from src.clean_data import clean_scores

def test_clean_scores_removes_nan():
    # Mock DataFrame with NaN in 'score'
    df = pd.DataFrame({
        'Student Name': ['Alice', 'Bob', 'Carol'],
        'Score': [95, None, 87]
    })

    cleaned = clean_scores(df)
    
    # After cleaning, there should be only 2 rows
    assert len(cleaned) == 2
    assert cleaned['score'].notnull().all()

def test_clean_scores_renames_columns():
    # Column with space in name
    df = pd.DataFrame({
        'Student Name': ['Alice'],
        'Test Score': [88]
    })
    
    cleaned = clean_scores(df)
    assert 'test_score' in cleaned.columns or 'score' in cleaned.columns
