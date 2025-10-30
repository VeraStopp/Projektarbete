def calculating_revenue_city(df):
    result_city = df.groupby("city")["revenue"].sum().reset_index()
    result_city = result_city.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return result_city

def calculate_category_rev(df):
    result_cat = df.groupby("category")["revenue"].sum().reset_index()
    result_cat = result_cat.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return result_cat

def calculate_average_order_value(df):   
    total_revenue = df["revenue"].sum()             #get total revenue from CSV 
    total_unique_orders = df['order_id'].nunique()  #get total unique orders from CSV
    return total_revenue / total_unique_orders

def calculate_total_revenue(df):
    return float(df["revenue"].sum())

def calculate_total_units(df):
    return int(df["units"].sum())

    