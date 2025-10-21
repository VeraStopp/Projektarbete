import matplotlib.pyplot as plt

def plot_revenue_by_category(revenue_by_category):
    plt.bar(revenue_by_category['category'], revenue_by_category['revenue'])   # Create a bar chart
    plt.title("Intäkt per kategori") # Set the title of the plot   
    plt.xlabel("Kategori") # Set the x-axis label
    plt.ylabel("Intäkt") # Set the y-axis label
    plt.show()  # Display the plot