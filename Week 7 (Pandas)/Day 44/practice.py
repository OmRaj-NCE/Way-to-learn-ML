import pandas as pd

df = pd.read_csv("students.csv")

print("\n--- DATA PREVIEW ---")
print(df.head())

print("\n--- SHAPE ---")
print(df.shape)

print("\n--- INFO ---")
print(df.info())

print("\n--- STATISTICS ---")
print(df.describe())

print("\n--- AVERAGE MARKS ---")
print(df["Marks"].mean())

print("\n--- TOP STUDENT ---")
top = df[df["Marks"] == df["Marks"].max()]
print(top)
