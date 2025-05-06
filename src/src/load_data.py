import pandas as pd

def load_test_results(file_path):
    """Load test results from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        raise
