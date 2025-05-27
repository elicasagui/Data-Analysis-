# tests/test_load_data.py

import os
import pandas as pd
import pytest
from src.load_data import load_test_results

def test_load_test_results_success(tmp_path, capsys):
    # Crear un CSV de prueba
    data = pd.DataFrame({'borough': ['A'], 'score': [100]})
    file = tmp_path / "test.csv"
    data.to_csv(file, index=False)

    # Cargar datos
    df = load_test_results(str(file))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 2)
    captured = capsys.readouterr()
    assert "Loaded data shape" in captured.out

def test_load_test_results_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_test_results("nonexistent.csv")
