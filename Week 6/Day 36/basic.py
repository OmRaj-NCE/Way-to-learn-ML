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
# print(np.arange(1,21,1))
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


# --------------------------------------------------------

# 🧠 1. Array vs List (Deep Difference)
# Python List
# l = [1,2,3]
# NumPy Array
# a = np.array([1,2,3])
# 🔥 Key Difference
# Feature	List	NumPy
# Speed	    Slow	Fast
# Type	    Mixed	Same type
# Math	    Manual  loop	Vectorized
# Memory	High	Efficient


# 🧠 2. Homogeneous Nature (VERY IMPORTANT)
arr = np.array([1, 2, 3.5])
print(arr)
# Output: # [1.  2.  3.5]
# 👉 NumPy converts everything to same datatype


# 🧠 3. dtype Control (ADVANCED)
arr = np.array([1,2,3], dtype=int)
arr1 = np.array([1,2,3], dtype=float)
print(arr)
print(arr1)
# 👉 Forces datatype


# 🧠 4. Vectorized Operations (CORE ML SKILL)
arr = np.array([1,2,3])
print(arr + 5)
print(arr * 2)
print(arr ** 2)
# No loops → very important


# 🧠 5. Array + Array Operations
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)
print(a * b)
# 👉 Element-wise operations


# 🧠 6. Comparison Operations
arr = np.array([10, 20, 30])
print(arr > 15)
# Output: [False True True]
# 👉 Used in ML filtering


# 🧠 7. Boolean Indexing (VERY IMPORTANT)
arr = np.array([10, 20, 30, 5])
print(arr[arr > 10])
# Output: [20 30]
# 👉 This replaces loops in ML pipelines


# 🧠 8. Built-in Functions
arr = np.array([1,2,3,4])
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())


# 🧠 9. Shape Understanding
arr = np.array([1,2,3])
print(arr.shape)
# Output: (3,)
# 👉 1D array = vector
arr = np.array([[1,2,3],[1,2,3]])
print(arr.shape)
arr = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(arr.shape)


# 🛠️ 🔥 ADVANCED MINI TASK (DO THIS)
# Modify your program:
# Add:
# Print numbers greater than average
# Print only even numbers using NumPy (no loop)
# Print sum, mean, max, min
# Convert array to float type
n1 = []
while True:
    n2 = input("Enter a number or 'quit': ")
    if n2 == 'quit':
        break
    try:
        # if n2 == '' or n2 == ' ' or len(n2) == 0:
        #     print("No number")
        #     break
        n1.append(int(n2))
    except ValueError:
        print("Invalid input")
arr = np.array(n1)
print(arr)
avg = arr.mean()
print(avg)
print(arr[avg < arr])
print(arr[arr % 2 == 0])
print(arr.max(), arr.min(), arr.mean(), arr.sum())
arr_float = np.array(arr, dtype=float)
print(arr_float)
