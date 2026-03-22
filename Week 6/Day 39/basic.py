# 📅 DAY 39 — Advanced Broadcasting & Axis Operations (ML-Level)
# 🎯 Objective (Advanced)
# By the end of today, you will:
# Understand axis (0 vs 1) deeply
# Perform row-wise vs column-wise operations
# Apply broadcasting on matrices
# Do feature scaling like ML pipelines
# Think in terms of datasets, not arrays

# 🧠 PART 1 — What is “Axis”? (VERY IMPORTANT)
# Consider:
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
# Shape: (2 rows, 3 columns)
# Axis    Meaning:
# Axis	Meaning
# axis=0	down (column-wise)
# axis=1	across (row-wise)

# Example:
print(arr.sum(axis=0))
# Output: [50 70 90]
# 👉 Column-wise sum

print(arr.sum(axis=1))
# Output: [60 150]
# 👉 Row-wise sum



# 🧠 PART 2 — Why Axis Matters in ML
# Dataset:
# rows → samples (students, users)
# columns → features (age, salary, marks)
# 👉 axis=0 → feature-wise
# 👉 axis=1 → sample-wise

# 🧠 PART 3 — Column-Wise Mean (VERY IMPORTANT)
mean = arr.mean(axis=0)
print(mean)
# Output: [25 35 45]
# 👉 Mean of each column (feature)



# 🔥 PART 4 — Feature Normalization (CORE ML)
arr = np.array([
    [10,20,30],
    [40,50,60]
])
mean = arr.mean(axis=0)
mean1 = arr.mean(axis=1)
print(f"\n{mean}\n")
print(f"\n{mean1}\n")
normalized = arr - mean
print(normalized)
# Output: [[-15 -15 -15]
#          [ 15  15  15]]
# 👉 This is feature centering


# 🧠 PART 5 — How Broadcasting Works Here
# arr (2,3)
# mean (3,)
# NumPy converts mean → (1,3) automatically
# Then subtracts from each row.


# 🔥 PART 6 — Row-wise Operations
# print(arr.sum(axis=1))
# 👉 Used for:
# total per user
# total per row


# 🔥 PART 6 — Row-wise Operations
print(arr.sum(axis=1))
# 👉 Used for:
# total per user
# total per row


# 🧠 PART 7 — Keep Dimensions (Advanced)
mean = arr.mean(axis=0, keepdims=True)
mean1 = arr.mean(axis=1, keepdims=True)
mean2 = arr.mean(axis=1, keepdims=False)
print(mean)
print(mean1)
print(mean2)
# Output: [[25 35 45]]
# 👉 Keeps shape → useful for broadcasting


# 🧠 PART 9 — Filtering Rows (Dataset Logic)
arr = np.array([
    [10,20,30],
    [40,50,60]
])
high = arr[arr[:,1] > 30]
print(high)
# 👉 Filter rows based on feature





# Slicing from Bro Code
# take 4 rows * 4 cols [[],[],[],[]]
array =np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
# array[start:end:step]

# Row print
print(array[1])
print()
print(array[0])
print()
print(array[3])
print()
print(array[-1])
print()

# Row print
print(array[0:3])
print()
print(array[1:4])
print()
print(array[0:4:2])
print()
print(array[::2])
print()
print(array[::-1])
print()
print(array[::-2])

# Column print
# print(array[0 , 0]) first for row & second for column
print(array[:,0])
print()
print(array[:,2])
print()
print(array[:,-2])
print()
print(array[:,0:3])
print()
print(array[:,1:3])
print()
print(array[:,::2])
print()
print(array[:,1::2])
print()
print(array[:,::-1])

# First two rows first columns
print(array[0:2,0:2])
print()
print(array[0:2,2:4])
print()
print(array[0:2,2:])
