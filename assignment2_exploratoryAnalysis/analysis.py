import pandas as pd

df = pd.read_csv("data/Sales-Export_2019-2020.csv")

print("Rows and Columns:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nOrder Value Statistics:")
print("Count:", df["Order_Value_EUR"].count())
print("Mean:", df["Order_Value_EUR"].mean())
print("Median:", df["Order_Value_EUR"].median())
print("Minimum:", df["Order_Value_EUR"].min())
print("Maximum:", df["Order_Value_EUR"].max())
print("Standard Deviation:", df["Order_Value_EUR"].std())

print("\nCost Statistics:")
print("Count:", df["Cost"].count())
print("Mean:", df["Cost"].mean())
print("Median:", df["Cost"].median())
print("Minimum:", df["Cost"].min())
print("Maximum:", df["Cost"].max())
print("Standard Deviation:", df["Cost"].std())

print("\nSales by Category:")
category_sales = df.groupby("Category")["Order_Value_EUR"].sum()
print(category_sales)

print("\nSales by Country:")
country_sales = df.groupby("Country")["Order_Value_EUR"].sum()
print(country_sales)

print("\nSales by Device:")
device_sales = df.groupby("device_type")["Order_Value_EUR"].sum()
print(device_sales)

highest=df["Order_Value_EUR"].max()
lowest=df["Order_Value_EUR"].min()

print("\nHighest Order:")
print(highest)
print(df[df["Order_Value_EUR"] == highest])

print("\nLowest Order:")
print(lowest)
print(df[df["Order_Value_EUR"] == lowest])

Average=df["Order_Value_EUR"].mean()

print("\nAverage Order Value:")
print(Average)

if average >= 100:
    print("Average order value meets the goal.")
else:
    print("Average order value is below the goal.")

total_sales = df["Order_Value_EUR"].sum()

print("\nSummary:")
print("Total Sales:", total_sales)
print("Average Order:", Average)
print("Highest Order:", highest)
print("Lowest Order:", lowest)

print("Best Selling Category:", category_sales.idxmax())
print("Country with Most Sales:", country_sales.idxmax())
print("Device with Most Sales:", device_sales.idxmax())