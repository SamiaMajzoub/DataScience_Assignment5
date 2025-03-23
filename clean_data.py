import pandas as pd

df = pd.read_csv("ebay_tech_deals.csv", dtype=str)
# df.head()

df["Price"] = df["Price"].astype(str)
df["Original_price"] = df["Original_price"].astype(str)


for col in ["Price", "Original_price"]:
    df[col] = (
        df[col]
        .str.replace("US $", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

# df.head(100)

df["Original_price"].fillna(df["Price"], inplace=True)
# df.head(100)

df['Shipping'] = df['Shipping'].replace(["N/A", "", None], "Shipping info unavailable").str.strip()
# df.head(100)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Original_price"] = pd.to_numeric(df["Original_price"], errors="coerce")

df["Discount_percentage"] = (
    (1 - (df["Price"] / df["Original_price"])) * 100
).round(2)

# df.head(100)

#We can see that some products still remain (are not sold) if they are duplicated trhoughout the automation period of 5 days (from 19 till 23 March)
#Number of duplicate rows: 2665 is the result of the following code

df.duplicated().sum()
df_notimpstamp = df.drop(columns=['Timestamp'])
num_duplicates = df_notimpstamp.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")


df.to_csv("cleaned_ebay_deals.csv", index=False)