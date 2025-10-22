import pandas as pd 

def load_data(path="data/ecommerce_sales.csv"):
    df = pd.read_csv(path)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df
