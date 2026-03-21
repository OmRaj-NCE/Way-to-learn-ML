# 🧠 PART 1 — Install NumPy
# Run this once:
# pip install numpy

# 🧠 PART 2 — Import NumPy
import numpy as np
# 👉 np is standard alias (used everywhere in ML)

# 📦 PART 3 — Creating Arrays
# From list
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

# 🔍 PART 4 — Array Properties
print(arr.shape)   # size
print(arr.ndim)    # dimensions
print(arr.dtype)   # data type

# 🧠 PART 5 — Why NumPy > Lists
# Python list
nums = [1, 2, 3]
result = []
for n in nums:
    result.append(n * 2)
    
# NumPy array
arr = np.array([1, 2, 3])
result = arr * 2
# ✔ No loop
# ✔ Faster
# ✔ Cleaner
# This is called vectorization.

# 🔢 PART 6 — Creating Special Arrays
np.zeros(5)
np.ones(5)
np.arange(1, 10)
np.linspace(0, 1, 5)

# Create array from input list
# Multiply all elements by 5
# Create array from 1–20
# Create array of 10 zeros
# Print shape and datatype
# num1 = []
# while True:
#     num = input("Enter you number or 'quit': ")
#     if num == 'quit'.lower():
#         break
#     if num != 'quit':
#         num1.append(int(num))
# arr = np.array(num1)
# print(arr)
# arr_mul5 = arr * 5
# print(arr_mul5)
# print(np.arange(0,21,1))
# print(np.zeros(10))
# print("Shape:", arr.shape)
# print("Datatype:", arr.dtype)

num1 = []
while True:
    num = input("Enter number or 'quit': ")
    if num.lower() == 'quit':
        break
    try:
        num1.append(int(num))
    except ValueError:
        print("Invalid input, try again")
arr = np.array(num1)
print(arr)
