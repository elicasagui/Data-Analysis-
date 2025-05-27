# tests/test_analyze.py

import pandas as pd
import pytest
from src.analyze import average_scores_by_borough

def test_average_scores_by_borough_correct():
    df = pd.DataFrame({
        'borough': ['X', 'Y', 'X'],
        'score': [10, 20, 30]
    })
    result = average_scores_by_borough(df)
    # X → (10+30)/2 = 20, Y → 20
    assert list(result.index) == ['X', 'Y']
    assert pytest.approx(result['X']) == 20
    assert pytest.approx(result['Y']) == 20

def test_average_scores_by_borough_missing_columns():
    df = pd.DataFrame({'other': [1, 2]})
    with pytest.raises(ValueError):
        average_scores_by_borough(df)
