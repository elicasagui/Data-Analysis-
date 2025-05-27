# tests/test_clean_data.py

import pandas as pd
import pytest
from src.clean_data import clean_scores

def test_clean_scores_removes_nan_and_coerces():
    df = pd.DataFrame({
        'score': [95, None, '87', 'invalid']
    })
    cleaned = clean_scores(df)
    # Deberían quedarse solo 95 y 87 convertidos a numérico
    assert cleaned['score'].dtype.kind in ('i', 'f')
    assert len(cleaned) == 2
    assert set(cleaned['score']) == {95, 87}

def test_clean_scores_normalizes_column_names_and_keeps_other_cols():
    df = pd.DataFrame({
        'Student Name': ['Alice'],
        'Test Score': [88]
    })
    # Después de limpiar, 'test_score' existe y mantiene otras columnas
    cleaned = clean_scores(df)
    assert 'test_score' in cleaned.columns
    assert 'student_name' in cleaned.columns
