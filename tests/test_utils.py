# tests/test_utils.py

import os
from src.utils import get_data_path

def test_get_data_path_joins_correctly():
    filename = "myfile.csv"
    path = get_data_path(filename)
    # Debe corresponder a data/myfile.csv (o data\myfile.csv en Windows)
    assert os.path.normpath(path) == os.path.normpath(os.path.join("data", filename))
