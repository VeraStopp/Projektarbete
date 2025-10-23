def calculating_revenue_city(df):
    result_city = df.groupby("city")["revenue"].sum().reset_index()
    result_city = result_city.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return result_city

def calculate_category_rev(df):
    result_cat = df.groupby("category")["revenue"].sum().reset_index()
    result_cat = result_cat.sort_values(by="revenue", ascending=False)
    return result_cat

def calculate_average_order_value(df):   
    total_revenue = df['revenue'].sum()             #get total revenue from CSV 
    total_unique_orders = df['order_id'].nunique()  #get total unique orders from CSV


    average_order_value = total_revenue / total_unique_orders

    return average_order_value, total_revenue

def calculate_revenue_by_category(df):

    calculate_revenue_by_category = df.groupby("category")["revenue"].sum().reset_index()
    calculate_revenue_by_category = calculate_revenue_by_category.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return calculate_revenue_by_category


    
