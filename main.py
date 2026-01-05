import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("/content/sales_data.csv")
df

# BASIC ANALYSIS
total_revenue = df["Total_Sales"].sum()
product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nTotal Revenue:", total_revenue)
print("\nSales by Product:")
print(product_sales)

import os

# VISUALIZATION 1: BAR CHART
plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
os.makedirs('visualizations', exist_ok=True)
plt.savefig("visualizations/sales_by_product.png")
plt.show()

import os

# VISUALIZATION 2: PIE CHART
category_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution by Product")
plt.ylabel("")
plt.tight_layout()
os.makedirs('visualizations', exist_ok=True)
plt.savefig("visualizations/revenue_distribution.png")
plt.show()

