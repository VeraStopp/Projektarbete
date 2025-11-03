import pandas as pd

def load_data(filepath):
    """
    Load CSV file, parse the "date" column as datetime and clean the column names.
    """
    df = pd.read_csv(filepath, parse_dates=["date"])
    df.columns = (df.columns.str.strip().str.replace(" ", "_").str.lower())
    return df