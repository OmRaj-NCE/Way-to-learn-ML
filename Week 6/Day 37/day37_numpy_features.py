import numpy as np

data = []

n = int(input("How many records? "))

for i in range(n):
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    data.append([age, salary])

arr = np.array(data)

ages = arr[:, 0]
salaries = arr[:, 1]

print("\nAges:", ages)
print("Salaries:", salaries)

# filter high salary (>50000)
high_salary = arr[arr[:,1] > 50000]

print("\nHigh salary records:")
print(high_salary)
