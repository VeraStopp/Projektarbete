import matplotlib.pyplot as plt                                                       


def plot_revenue_by_category(calculate_category_rev):                           
    """
    Creating av bar chart for revenue per catagory
    """
    plt.bar(calculate_category_rev['category'], calculate_category_rev['revenue'])  
    plt.title("Revenue for each category")                 
    plt.xlabel("Category")                           
    plt.ylabel("Revenue (MSEK)")    
    plt.show()                                                               

def plot_revenue_by_month(calculate_revenue_by_month):                                      
    """
    Creating a plot for revenue by month
    """
    calculate_revenue_by_month['month'] = calculate_revenue_by_month['month'].astype(str)         
    plt.plot(calculate_revenue_by_month['month'], calculate_revenue_by_month['revenue'])        
    data_to_plot = calculate_revenue_by_month.set_index('month')                             
    plt.title("Revenue over time") 
    plt.xlabel("Time(month)") 
    plt.ylabel("Revenue (SEK)") 
    plt.grid(True)                                                                              
    plt.show()                                                                                    


# Function to plot monthly revenue per category
def plot_monthly_category_revenue(calculate_monthly_category_revenue):                                        
    """
    Creating av plot for revenue per month and catagory
    """
    calculate_monthly_category_revenue['month'] = calculate_monthly_category_revenue['month'].astype(str)      
    categories = calculate_monthly_category_revenue['category'].unique()                                     
    for category in categories:                                                                             
        category_data = calculate_monthly_category_revenue[calculate_monthly_category_revenue['category'] == category]
        plt.plot(category_data['month'], category_data['revenue'], label=category)                        

    plt.title("Monthly revenue for each catagory")                                                
    plt.xlabel("Time (month)")                                                             
    plt.ylabel("Revenue (SEK)")                                                                
    plt.legend(title="Kategori")                                                             
    plt.grid(True)                                                                         
    plt.show()                                                                               