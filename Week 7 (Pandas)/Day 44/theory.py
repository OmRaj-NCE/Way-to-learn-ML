# 📅 DAY 44 — Reading CSV & Data Exploration (DEEP)

# What is CSV
# Example : 
# Create a file named std.csv
# Name,Marks,Cousre
# Raj,85,AIML
# Aman,82,CSE
# Sita,91,AIML
# Ravi,60,CSE
import pandas as pd
df = pd.read_csv("std.csv")
print(df)

# Data Inspection
print(df.head())
print(df.head(0))
print(df.tail())    
print(df.shape)  
print()
print(df.columns)
print()
print(df.dtypes)
print()
print(df.info())
print()
print(df.describe())

print()
# Selecting Data
# Single Column
print(df["Marks"])
# Multiple column
print(df[["Name","Marks"]])

print()
# Quick Analysis
print("Avg Marks: ", df["Marks"].mean())
print("Max Marks: ", df["Marks"].max())
