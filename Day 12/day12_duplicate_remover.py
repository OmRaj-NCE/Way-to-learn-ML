data = []
n = int(input("How many values? "))
for i in range(n):
    value = input(f"Enter value {i+1}: ")
    data.append(value)
unique_values = set(data)
print("\nOriginal List:", data)
print("Unique Values:", unique_values)
print("Total Unique:", len(unique_values))
