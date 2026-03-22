# 📅 DAY 38 — Vectorization & Broadcasting (DEEP LEVEL)
# 🎯 Objective
# By the end of today, you will:
# Understand broadcasting deeply
# Perform array + scalar operations
# Perform array + array operations (different shapes)
# Build ML-style transformations
# Replace loops completely

# 🧠 PART 1 — What is Broadcasting?
# 👉 Broadcasting =
# Automatically expanding smaller array to match bigger one
# So operations can happen without loops.

# 🧪 PART 2 — Scalar Broadcasting (Easy Start)
# import numpy as np
arr = np.array([1,2,3])
print(arr + 5)
# Output: [6 7 8]
# What happens internally:
# [1 2 3]
# +5 → [5 5 5]
# ---------
# [6 7 8]
# ✔ NumPy auto-expands 5 → [5,5,5]

# 🧠 PART 3 — Array + Array (Same Shape)
a = np.array([1,2,3])
b = np.array([10,20,30])
print(a + b)
# Output: [11 22 33]
# 👉 Element-wise operation

# 🔥 PART 4 — Broadcasting with Different Shapes
a = np.array([1,2,3])
b = np.array([10])
print(a + b)
# Output: [11 12 13]
# 👉 [10] becomes [10,10,10]

# 🧠 PART 5 — 2D Broadcasting (VERY IMPORTANT)
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr + 10)
# Output: [[11 12 13]
#          [14 15 16]]

# 🧠 PART 9 — Real ML Example
# Normalize data
arr = np.array([10,20,30])
norm = arr / max(arr)
print(norm)
# Output: [0.33 0.66 1.0]
