import numpy as np

nums = []

n = int(input("How many numbers? "))

for i in range(n):
    nums.append(int(input(f"Enter number {i+1}: ")))

arr = np.array(nums)

print("\nArray:", arr)
print("Shape:", arr.shape)
print("Datatype:", arr.dtype)

print("\nMultiplied by 2:", arr * 2)
print("Squared:", arr ** 2)
