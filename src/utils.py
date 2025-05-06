import os

def get_data_path(filename):
    """Return relative path to data file."""
    return os.path.join("data", filename)
