import pandas as pd

names = []
marks = []

n = int(input("How many students? "))

for i in range(n):
    names.append(input("Name: "))
    marks.append(int(input("Marks: ")))

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("\nStudent Data:\n")
print(df)

print("\nTop 2 Students:\n")
print(df.head(2))
