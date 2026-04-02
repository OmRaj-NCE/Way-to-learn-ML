# install pandas
# pip install pandas
# import pandas as pd

# What is series
import pandas as pd
s = pd.Series([10,20,30])
print(s)

# DataFrame
print()
print("DataFrame")
data = {
    "Name":["Raj","Aman","Sita"],
    "Marks":[85,89,93]
}
df = pd.DataFrame(data)
print(df)

print()
print("Structure")
print("Shape: ",df.shape)
print("Column: ",df.columns)
print("Head: ",df.head())

print()
# Accessing Data
print("Accessing Data")
print("Column")
print("df[\"Marks\"] :\n",df["Marks"])

print("Rows")
print(df.iloc[0])
print(df.iloc[1])

# 🧠 PART 6 — Add New Column
print("Add New Column")
df["Grade"] = ["A","B","C"]
