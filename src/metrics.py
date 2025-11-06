import pandas as pd                               #importing pandas library for data manipulation   

def summary_city(df):
    return (df.groupby("city")
            .agg(
                antal_ordrar = ("city", "count"),
                medelvärde_vinst = ("revenue", "mean"),
                median_vinst = ("revenue", "median"),
                std_vinst = ("revenue", "std")
            ).reset_index())

def calculate_revenue_city(df):
    result = df.groupby("city")["revenue"].sum().reset_index()
    result = result.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return result

def summary_category(df):
    return (df.groupby("category")
            .agg(
                antal_ordrar = ("category", "count"),
                medelvärde_vinst = ("revenue", "mean"),
                median_vinst = ("revenue", "median"),
                std_vinst = ("revenue", "std")
            ).reset_index())

def calculate_category_rev(df):
    summary = df.groupby("category")["revenue"].sum().reset_index()
    summary = summary.sort_values(by="revenue", ascending=False)
    return summary

def calculate_average_order_value(df):   
    total_revenue = df['revenue'].sum()             #get total revenue from CSV 
    total_unique_orders = df['order_id'].nunique()  #get total unique orders from CSV
    average_order_value = total_revenue / total_unique_orders
    return round(average_order_value, 2)

def calculate_total_revenue(df):
    total_revenue = float(df['revenue'].sum())
    return round(total_revenue, 2)

def calculate_total_units(df):
    total_units = int(df['units'].sum())
    return round(total_units, 2)


def calculate_revenue_by_month(df):

    #I need to convert the date column to a monthly format 
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M') 

    revenue_by_month = df.groupby("month")["revenue"].sum().reset_index()  #group by date and sum revenue (how to do it by month?? created month column and grouped by it)
    revenue_by_month = revenue_by_month.sort_values(by ="month") #sort by date

    return revenue_by_month



# New function to calculate monthly revenue per category
def calculate_monthly_category_revenue(df):     #defining a function to calculate monthly revenue per category

    # Convert the date column to a monthly format
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')

    monthly_category_revenue = df.groupby(['month', 'category'])['revenue'].sum().reset_index()  #group by month and category, summing revenue
    monthly_category_revenue = monthly_category_revenue.sort_values(by=['month', 'category'])    #sort by month and category

    return monthly_category_revenue 