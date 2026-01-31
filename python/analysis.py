import pandas as pd

df = pd.read_csv("../data/cleaned_sales_data.csv")

# Top Products
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTop Products:")
print(top_products)

# Region-wise Revenue
region_sales = df.groupby("Region")["Sales"].sum()
print("\nRegion-wise Sales:")
print(region_sales)

# Monthly Sales Trend
df['Month'] = df['Order_Date'].astype(str).str[:7]
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)
