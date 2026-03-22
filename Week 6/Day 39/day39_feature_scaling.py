import numpy as np

data = []

n = int(input("How many records? "))

for i in range(n):
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    data.append([age, salary])

arr = np.array(data)

print("\nDataset:\n", arr)

# column-wise mean
mean = arr.mean(axis=0)

# normalization
normalized = arr - mean

# scaling
scaled = arr / arr.max(axis=0)

print("\nMean:", mean)
print("\nNormalized:\n", normalized)
print("\nScaled:\n", scaled)

# filter high salary
high_salary = arr[arr[:,1] > arr[:,1].mean()]

print("\nHigh salary records:\n", high_salary)
