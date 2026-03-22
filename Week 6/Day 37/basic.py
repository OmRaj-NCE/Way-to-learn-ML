# 📅 DAY 37 — Indexing & Slicing (DEEP LEVEL)
# 🎯 Objective (Advanced)
# By the end of today you will:
# Master 1D + 2D indexing
# Understand views vs copies
# Use boolean indexing like ML pipelines
# Extract features (columns/rows)
# Modify arrays efficiently

# 🧠 PART 1 — 1D Indexing (Quick but Important)
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr[0])    # 10
print(arr[-1])   # 40


# 🧠 PART 2 — 1D Slicing (Core Concept)
print(arr[1:3])   # [20 30]
print(arr[:2])    # [10 20]
print(arr[::2])   # [10 30]
# 👉 Same as Python lists — but faster


# 🔥 PART 3 — SLICING RETURNS VIEW (VERY IMPORTANT)
arr = np.array([1,2,3,4])
slice_arr = arr[1:3]
print(slice_arr)
slice_arr[0] = 100
print(arr)
# Output: [1 100 3 4]
# ⚠️ This is HUGE: NumPy slicing does NOT copy → it creates a view
# 🧠 To create copy:
copy_arr = arr[1:3].copy()
print(copy_arr)


# 🧠 PART 4 — 2D ARRAYS (REAL DATA)
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# Think of like this : rows X columns


# 🧠 PART 5 — 2D INDEXING
print(arr[0,0])   # 1
print(arr[1,2])   # 6
# 👉 Format: [row, column]


# 🧠 PART 6 — 2D SLICING (VERY IMPORTANT)
# Get first row
print(arr[0])
# Get first column
print(arr[:,0])
# Get sub-matrix
print(arr[0:2, 1:3])


# 🔥 PART 7 — BOOLEAN INDEXING (ML CORE)
arr = np.array([10, 20, 30, 5])
print(arr[arr > 10])
# Output: [20 30]
# Real ML-style filtering:
data = np.array([50, 80, 120, 30])
clean = data[data <= 100]
print(clean)
# 👉 Removing outliers


# 🧠 PART 8 — MODIFYING WITH CONDITION
arr = np.array([10, 20, 30])
arr[arr > 15] = 0
print(arr)
# Output: [10 0 0]
# 👉 Used in preprocessing


# 🧠 PART 9 — COLUMN SELECTION (DATASET THINKING)
data = np.array([
    [25, 50000],
    [30, 60000],
    [22, 45000]
])
# Extract age:
ages = data[:,0]
print(ages)
# Extract salary:
salary = data[:,1]
print(salary)
# 👉 This is feature extraction in ML
