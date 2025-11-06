import matplotlib.pyplot as plt                                                         # Importing matplotlib for plotting

# Graf 1 - Revenue by category
def plot_revenue_by_category(calculate_category_rev):                                # Defining a function to plot revenue by category
   
    plt.bar(calculate_category_rev['category'], calculate_category_rev['revenue'])      # Create a bar chart
    plt.title("Omsättning per kategori")                                                    # Set the title of the plot                  
    plt.xlabel("Kategori")                                                              # Set the x-axis label                           
    plt.ylabel("Omsättning (MSEK)")                                                         # Set the y-axis label
    plt.show()                                                                          # Display the plot

# Graf 2 - Försäljning över tid
def plot_revenue_by_month(calculate_revenue_by_month):                                              # Defining a function to plot revenue by month   
  
    calculate_revenue_by_month['month'] = calculate_revenue_by_month['month'].astype(str)           # Convert 'month' to string for better x-axis labeling
    
    plt.plot(calculate_revenue_by_month['month'], calculate_revenue_by_month['revenue'])            # line plot of revenue over months
    
    data_to_plot = calculate_revenue_by_month.set_index('month')                                    # Set 'month' as the index for easier plotting ??????
    
    plt.title("Försäljning över tid (månasvis") 
    plt.xlabel("Tid(månad)") 
    plt.ylabel("Omsättning (SEK)") 
    plt.grid(True)                                                                                  # Add grid for better readability
    plt.show()                                                                                      # Display the plot



# Graf 3 - Spridningen
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