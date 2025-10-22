def calculating_revenue_city(df):
    result = df.groupby("city")["revenue"].sum().reset_index()
    result = result.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return result

def calculate_category_rev(df):
    summary = df.groupby("category")["revenue"].sum().reset_index()
    summary = summary.sort_values(by="revenue", ascending=False)
    return summary

def calculate_average_order_value(df):   
    total_revenue = df['revenue'].sum()             #get total revenue from CSV 
    total_unique_orders = df['order_id'].nunique()  #get total unique orders from CSV


    average_order_value = total_revenue / total_unique_orders

    return average_order_value, total_revenue

def calculate_total_revenue(df):
    return float(df['revenue'].sum())

def calculate_total_units(df):
    return int(df['units'].sum())
