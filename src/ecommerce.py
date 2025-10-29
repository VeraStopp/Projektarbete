import pandas as pd

class EcommerceAnalyzer:
    def __init__(self, df):
        self.df = df

    def calculating_revenue_city(self):
        result_city = self.df.groupby("city")["revenue"].sum().reset_index()
        result_city = result_city.sort_values(by="revenue", ascending=False).reset_index(drop=True)
        return result_city
    

test = EcommerceAnalyzer(pd.read_csv("./data/ecommerce_sales.csv"))

print(test.calculating_revenue_city())