import pandas as pd

# Load raw data
df = pd.read_csv("../data/raw_sales_data.csv")

print("Raw Data:")
print(df)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert Order_Date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Handle missing values
df.fillna(0, inplace=True)

# Save cleaned data
df.to_csv("../data/cleaned_sales_data.csv", index=False)

print("\nCleaned Data Saved Successfully!")
