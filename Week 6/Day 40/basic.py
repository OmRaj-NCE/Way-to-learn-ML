# 📅 DAY 40 — NumPy Statistics (ML Core Math)
# 🎯 Objective (Very Important)
# By the end of today, you will:
# Understand mean, median, variance, std
# Perform statistical analysis on datasets
# Apply standardization (Z-score)
# Think in terms of data distribution
# Prepare data for ML models

# 🧠 PART 1 — Why Statistics Matter in ML
# ML models depend on:
# data distribution
# spread of values
# feature scaling
# Without stats → models perform poorly.


# 🧠 PART 2 — Basic Statistics
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# Mean (average)
print(arr.mean())
# 👉 Center of data

# Median
print(np.median(arr))
# 👉 Middle value (robust to outliers)

# Min / Max
print(arr.min())
print(arr.max())


print()
# 🧠 PART 3 — Variance & Standard Deviation (VERY IMPORTANT)
# Variance
print(arr.var())
# 👉 How spread out data is

# Standard Deviation
print(arr.std())
# 👉 Average distance from mean
# Example (Sample Data: 5, 10, 15)
# Mean: (5+10+15)/3 = 10
# Deviation: (5-10)= -5, (10-10)= 0, (15-10)= 5
# Sq Deviation: (-5)^2=25, (0)^2=0, (5)^2= 25
#  sum of sq: 25+0+25= 50
# variance (n-1): 50/(3-1) = 25
# std deviation: under root(25) = 5



# 🔥 PART 5 — Z-SCORE STANDARDIZATION (CORE ML)
# Formula:
# (value - mean) / std
# Example:
arr = np.array([10,20,30,40,50])
mean = arr.mean()
std = arr.std()
z = (arr - mean) / std
print(z)
# Output (approx):
# [-1.41 -0.70 0 0.70 1.41]
# 👉 Now data is:
# centered at 0
# scaled


# 🧠 PART 7 — Column-wise Statistics (IMPORTANT)
arr = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
])
# Mean per feature:
print(arr.mean(axis=0))
# Std per feature:
print(arr.std(axis=0))



# 🔥 PART 8 — Dataset Standardization
mean = arr.mean(axis=0)
std = arr.std(axis=0)
standardized = (arr - mean) / std
print(standardized)
# 👉 This is used in:
# Linear Regression
# Logistic Regression
# Neural Networks
