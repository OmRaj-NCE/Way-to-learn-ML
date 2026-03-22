import numpy as np

data = []

n = int(input("How many records? "))

for i in range(n):
    x = int(input("Feature 1: "))
    y = int(input("Feature 2: "))
    data.append([x, y])

arr = np.array(data)

print("\nDataset:\n", arr)

mean = arr.mean(axis=0)
std = arr.std(axis=0)

standardized = (arr - mean) / std

print("\nMean:", mean)
print("Std:", std)

print("\nStandardized data:\n", standardized)

# check distribution
print("\nNew mean:", standardized.mean(axis=0))
print("New std:", standardized.std(axis=0))
