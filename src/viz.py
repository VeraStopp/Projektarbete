import matplotlib.pyplot as plt                                                         # Importing matplotlib for plotting



#  Function to plot revenue by category
def plot_revenue_by_category(calculate_category_rev):                                   # Defining a function to plot revenue by category

    plt.bar(calculate_category_rev['category'], calculate_category_rev['revenue'])      # Create a bar chart

    # Adding titles and labels

    plt.title("Intäkt per kategori")                                                    # Set the title of the plot                  
    plt.xlabel("Kategori")                                                              # Set the x-axis label                           
    plt.ylabel("Intäkt (MSEK)")                                                         # Set the y-axis label
    plt.show()                                                                          # Display the plot



# Function to plot revenue by month
def plot_revenue_by_month(calculate_revenue_by_month):                                              # Defining a function to plot revenue by month   
    
    calculate_revenue_by_month['month'] = calculate_revenue_by_month['month'].astype(str)           # Convert 'month' to string for better x-axis labeling

    plt.plot(calculate_revenue_by_month['month'], calculate_revenue_by_month['revenue'])            # line plot of revenue over months

    data_to_plot = calculate_revenue_by_month.set_index('month')                                    # Set 'month' as the index for easier plotting ??????


    #   add titles and labels 
    plt.title("Försäljning över tid") 
    plt.xlabel("Tid(månad)") 
    plt.ylabel("Intäkt (kr)") 

    plt.grid(True)                                                                                  # Add grid for better readability

    plt.show()                                                                                      # Display the plot


# Function to plot monthly revenue per category
def plot_monthly_category_revenue(calculate_monthly_category_revenue):                                          # Defining a function to plot monthly revenue per category


    calculate_monthly_category_revenue['month'] = calculate_monthly_category_revenue['month'].astype(str)       # Convert 'month' to string for better x-axis labeling


    categories = calculate_monthly_category_revenue['category'].unique()                                        # Get unique categories

    for category in categories:                                                                                 # Loop through each category
        category_data = calculate_monthly_category_revenue[calculate_monthly_category_revenue['category'] == category] # Filter data for the current category
        plt.plot(category_data['month'], category_data['revenue'], label=category)                              # Plot revenue for each category

    # Adding titles and labels
    plt.title("Månadsvis intäkt per kategori")                                                 # Set the title of the plot
    
    plt.xlabel("Tid (månad)")                                                                  # Set the x-axis label
    plt.ylabel("Intäkt (kr)")                                                                  # Set the y-axis label
    plt.legend(title="Kategori")                                                               # Add legend with title. assign color to each category
    plt.grid(True)                                                                             # Add grid for better readability

    plt.show()                                                                                 # Display the plot


# Function to plot number of orders by category
def plot_number_of_orders_by_category(calculate_number_of_orders_by_category):                     # Defining a function to plot number of orders by category
    plt.bar(calculate_number_of_orders_by_category['category'], calculate_number_of_orders_by_category['order_count']) # Create a bar chart

    # Adding titles and labels
    plt.title("Antal beställningar per kategori")                                             # Set the title of the plot
    plt.xlabel("Kategori")                                                                     # Set the x-axis label
    plt.ylabel("Antal beställningar")                                                          # Set the y-axis label
    
    plt.show()                                                                                 # Display the plot")

# Function to plot order value distribution
def plot_order_distribution(df):
    plt.figure(figsize=(10, 6))

    # Plot a histogram of the 'revenue' column
    # bins=50 creates 50 "buckets" for the data
    plt.hist(df['revenue'], bins=50, edgecolor='black') 


    max_value = df['revenue'].max() 
    ticks = range(0, int(max_value) + 1001, 1000)
    plt.xticks(ticks)


    plt.title("Spridning av Ordervärden")
    plt.xlabel("Ordervärde (kr)")
    plt.ylabel("Antal Ordrar")
    plt.show()