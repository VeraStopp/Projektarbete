def calculating_revenue_city(df):
    result = df.groupby("city")["revenue"].sum().reset_index()
    result = result.sort_values(by="revenue", ascending=False).reset_index(drop=True)
    return result

def calculate_category_rev(df):
    summary = df.groupby("category")["revenue"].sum().reset_index()
    summary = summary.sort_values(by="revenue", ascending=False)
    return summary
