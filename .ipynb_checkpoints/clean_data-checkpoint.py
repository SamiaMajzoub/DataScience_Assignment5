import pandas as pd

df = pd.read_csv("ebay_tech_deals.csv", dtype=str)

def clean_price(price):
    if pd.isna(price) or price == "N/A":
        return None
    price = price.replace("US $", "").replace(",", "").strip()
    return float(price) if price else None

df["price"] = df["price"].apply(clean_price)
df["original_price"] = df["original_price"].apply(clean_price)

# If original_price is missing, replace it with the corresponding price
df["original_price"].fillna(df["price"], inplace=True)

# Clean the shipping column
df["shipping"] = df["shipping"].apply(
    lambda x: "Shipping info unavailable" if pd.isna(x) or x.strip() == "" or x == "N/A" else x.strip()
)

# Convert price and original_price columns to numeric (float)
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["original_price"] = pd.to_numeric(df["original_price"], errors="coerce")

# Create a new column discount_percentage
df["discount_percentage"] = (
    (1 - (df["price"] / df["original_price"])) * 100
).round(2)

# Handle missing values in discount_percentage (e.g., when original_price is 0 or missing)
df["discount_percentage"].fillna(0, inplace=True)

# Save the cleaned data to a new CSV file
df.to_csv("cleaned_ebay_deals.csv", index=False)

print("Data cleaning and processing complete. Saved to cleaned_ebay_deals.csv.")