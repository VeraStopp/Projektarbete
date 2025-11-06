import pandas as pd

class EcommerceAnalyzer:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def show_info(self):
        print(self.csv_file.info())
        print(self.csv_file.describe())
    
    def total_revenue(self):
        revenue = float(self.csv_file["revenue"].sum())
        print(f"Totala vinsten är {revenue:.2f} kr")
    
    def total_units(self):
        units = int(self.csv_file["units"].sum())
        print(f"Totala antal units är {units} st")

    def revenue_city(self):
        result_city = self.csv_file.groupby("city")["revenue"].sum().reset_index()
        result_city = result_city.sort_values(by="revenue", ascending=False).reset_index(drop=True)
        print(result_city)
    
    def revenue_category(self):
        result_cat = self.csv_file.groupby("category")["revenue"].sum().reset_index()
        result_cat = result_cat.sort_values(by="revenue", ascending=False).reset_index(drop=True)
        print(result_cat)
    
    def average_order_value(self):   
        total_revenue = self.csv_file["revenue"].sum()             
        total_unique_orders = self.csv_file["order_id"].nunique() 
        average_order_value = total_revenue / total_unique_orders
        print(f"Average order value är {average_order_value:.2f}")

