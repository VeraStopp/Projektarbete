import pandas as pd

class EcommerceAnalyzer:
    def __init__(self, data_frame):
        self.df = data_frame
    
    def show_info(self):
        print(self.df.info())
        print(self.df.describe())
    
    def total_revenue(self):
        revenue = float(self.df["revenue"].sum())
        return revenue
    
    def total_units(self):
        units = int(self.df["units"].sum())
        return units

    def revenue_city(self):
        result_city = self.df.groupby("city")["revenue"].sum().reset_index()
        result_city = result_city.sort_values(by="revenue", ascending=False).reset_index(drop=True)
        return result_city
    
    def revenue_category(self):
        result_cat = self.df.groupby("category")["revenue"].sum().reset_index()
        result_cat = result_cat.sort_values(by="revenue", ascending=False).reset_index(drop=True)
        return result_cat
    
    def average_order_value(self):   
        total_revenue = self.df["revenue"].sum()             
        total_unique_orders = self.df["order_id"].nunique() 
        average_order_value = total_revenue / total_unique_orders
        return average_order_value

    def calculate_revenue_by_month(self):
            
            df_copy = self.df.copy() 
            df_copy['date'] = pd.to_datetime(df_copy['date'])
            df_copy['month'] = df_copy['date'].dt.to_period('M')
            
            revenue_by_month = df_copy.groupby("month")["revenue"].sum().reset_index()
            
            return revenue_by_month
