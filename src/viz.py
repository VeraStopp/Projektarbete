import matplotlib.pyplot as plt

def plot_revenue_by_category(calculate_category_rev):
    plt.bar(calculate_category_rev['category'], calculate_category_rev['revenue'])   # Create a bar chart
    plt.title("Intäkt per kategori") # Set the title of the plot   
    plt.xlabel("Kategori") # Set the x-axis label
    plt.ylabel("Intäkt (miljoner)") # Set the y-axis label
    plt.show()  # Display the plot