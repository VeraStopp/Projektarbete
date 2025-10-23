import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = (df.columns.str.strip().str.replace(" ", "_").str.lower())
    return df