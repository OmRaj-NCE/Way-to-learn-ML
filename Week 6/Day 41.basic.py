# 📅 DAY 41 — Matrices & Dot Product (ML CORE)
# 🎯 Objective (CRITICAL)
# By the end of today, you will:
# Understand 2D arrays as matrices
# Perform matrix multiplication
# Understand dot product deeply
# Connect NumPy to ML equations
# Build intuition for model computation

import numpy as np
# 🧠 PART 1 — What is a Matrix?
# arr = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# 👉 Shape: (2 rows, 3 columns)
# Think: rows → data points
#        columns → features


# 🧠 PART 2 — Element-wise vs Matrix Multiplication
# Element-wise:
# a * b
# Matrix multiplication:
# np.dot(a, b)
# 👉 These are NOT the same


# 🔥 PART 3 — Dot Product (CORE IDEA)
# Example:
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))
# Calculation: # 1×4 + 2×5 + 3×6 = 32


# 🧠 PART 4 — Why Dot Product Matters
# ML formula:
# y = w1*x1 + w2*x2 + w3*x3
# 👉 This is:
# np.dot(weights, features)


# 🧠 PART 5 — Matrix Multiplication
A = np.array([
    [1,2],
    [3,4]
])
B = np.array([
    [5,6],
    [7,8]
])
print(np.dot(A,B))
# Rule:
# (A rows × A cols) × (B rows × B cols)
# A cols MUST equal B rows


# 🧠 PART 6 — Shape Logic (VERY IMPORTANT)
# (2×3) × (3×2) → valid
# (2×3) × (2×2) → invalid


# 🔥 PART 7 — ML Interpretation
# X = dataset
# W = weights
# y = np.dot(X, W)
# 👉 This is how models compute predictions


# 🧠 PART 8 — Matrix + Vector (COMMON IN ML)
X = np.array([
    [1,2],
    [3,4]
])
W = np.array([10,20])
print(np.dot(X, W))
# Result: Row-wise dot product


# 🧠 PART 9 — Transpose (IMPORTANT)
# A.T
# 👉 flips rows ↔ columns
# Used in:
# ML math
# matrix alignment
