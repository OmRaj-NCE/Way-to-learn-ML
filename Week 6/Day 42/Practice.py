# NumPy = fast math on grids of numbers. Everything in ML is grids (matrices, tensors). NumPy is why Python can compete with C for speed.

# IMPORT - Always First Line
import numpy as np  # 'np' is universal alias — use it always

# # ARRAY CREATION — 7 ways to know
# # 1. From Python list
# a = np.array([1, 2, 3])           # 1D → shape (3,)
# b = np.array([[1,2],[3,4]])     # 2D → shape (2,2)

# # 2. Zeros / Ones / Full
# np.zeros((3,4))   # 3 rows, 4 cols, all 0.0
# np.ones((2,3))    # 2 rows, 3 cols, all 1.0
# np.full((2,2), 7) # fill with 7
# print(np.full((3,3), 7)) # fill with 7

# # 3. Range-based
# np.arange(0, 10, 2)    # [0,2,4,6,8] — like range()
# print(np.arange(1, 10, 2))    # [1,3,5,7,9] — like range()
# np.linspace(0, 1, 5)   # 5 evenly spaced from 0→1
# print(np.linspace(0, 1, 5))   # 5 evenly spaced from 0→1
# print(np.linspace(0, 2, 5))   # 5 evenly spaced from 0→2 # [0.  0.5 1.  1.5 2. ]
# print(np.linspace(1.34, 2, 7))   # 7 evenly spaced from 1.34→2 # [[1.34 1.45 1.56 1.67 1.78 1.89 2.  ]]

# # 4. Identity matrix (ML: initializing weights)
# np.eye(3)   # 3×3 identity
# print(np.eye(2))

# # 5. Random (most used in ML!)
# np.random.rand(3,4)      # uniform [0,1), shape 3×4
# print(np.random.rand(2,2))
# np.random.randn(3,4)     # standard normal (mean=0, std=1)
# print()
# print(np.random.randn(3,4))     # standard normal (mean=0, std=1)
# print()
# print(np.random.randn(2,2))     # standard normal (mean=0, std=1)
# print()
# np.random.randint(0,10,(3,3)) # random ints 0–9
# print(np.random.randint(0,10,(3,3))) # random ints 0–9

# # 6. Like-another (copy shape, new values)
# np.zeros_like(a)   # same shape as a, filled 0
# np.ones_like(a)    # same shape as a, filled 1

# # a = np.array([1, 2, 3]) 
# print(np.ones_like(a))    # same shape as a, filled 1
# # b = np.array([[1,2],[3,4]])
# print(np.ones_like(b))    # same shape as a, filled 1
# b = np.array([[1,2],[3,4],[5,6],[7,8]])
# print(np.ones_like(b))    # same shape as a, filled 1

# # 7. Diagonal
# np.diag([1,2,3])   # diagonal matrix from list
# print(np.diag([1,2,3]))   # diagonal matrix from list


# # KEY ATTRIBUTES — know these cold
# # shape                ndim                  size                    dtype
# # a.shape              a.ndim                a.size                  a.dtype
# # → (3, 4) rows×cols   → 2 (number of axes)  → 12 (total elements)   → float64 / int64


# # DTYPE — data types you must know
# np.array([1,2], dtype=np.float32)  # ML: use float32 to save memory
# np.array([1,2], dtype=np.int64)   # indices, labels
# np.array([1,2]).astype(np.float32)  # convert later

# A = np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# print(A[0:2, 1:3])
# print(A[::2, ::2])

# A = np.array([[1,2],[3,4],[5,6]])
# A[[0, 2]]     # → [[1,2],[5,6]]  rows 0 and 2
# A[[0,1],[1,0]] # → [2, 3]  A[0,1] and A[1,0]
# print(A[[0, 2],[1,0]])
# print(A[[0,2]])

# arr = np.array([[[1,2],[3,4],[5,6],[7,8]]])
# print(arr.ndim)


# Q1. Create and Inspect a 1D Array
# Problem:
# Create a NumPy array from the list [10, 20, 30, 40, 50]. Print its shape, dimension, and data type.
# Input:
# Python list
# Expected Output:
# Array
# Shape → (5,)
# Dimension → 1
# Data type
# Concepts Required:
# Array creation, .shape, .ndim, .dtype
arr1 = np.array([10,20,30,40,50])
print(f"The shape is : {arr1.shape}")
print(f"The size is : {arr1.size}")
print(f"The Dimension is : {arr1.ndim}")
print(f"The Data Type is : {arr1.dtype}")

# Q2. Convert List to 2D Array
# Problem:
# Convert the list [1,2,3,4,5,6] into a 2×3 NumPy array.
# Input:
# 1D list
# Expected Output:
        # [[1 2 3]
#         [4 5 6]]
# Concepts Required:
# Array creation, .reshape()
print()
arr2 = np.array([1,2,3,4,5,6])
print(f"After reshaping : \n{arr2.reshape(2,3)}\n")

# Q3. Extract Specific Elements
# Problem:
# Given:
# [[10, 20, 30],
#  [40, 50, 60],
#  [70, 80, 90]]
# Extract:
# 50
# Entire 2nd row
# Entire 3rd column
# Input:
# 2D array
# Expected Output:
# Values + slices
# Concepts Required:
# Indexing, slicing (2D)
arr3 = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print(f"Raw data: {arr3}\n")
print(arr3[1:2 , 1:2])
print("Entire 2nd row :\n",arr3[:,1])
# print(arr3[:,2])
print("Entire 3rd Column: \n",arr3[:,2:3])

# Q4. Replace Values Using Indexing
# Problem:
# Replace all elements in the last row of a 3×3 array with 0.
# Input:
# 3×3 array
# Expected Output:
# Last row becomes [0 0 0]
# Concepts Required:
# Indexing, assignment
print()
arr4 = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print(f"Raw data of arr4: {arr4}")
slice_arr4 = arr4[2]
slice_arr4[:] = [0,0,0]
print(arr4)

# Q5. Create Array Using Range
# Problem:
# Create an array from 1 to 20 (inclusive). Then reshape it into 4×5.
# Input:
# Range values
# Expected Output:
# 4×5 matrix
# Concepts Required:
# np.arange(), reshape
print()
arr5 = np.arange(1,21,1)
print(arr5.reshape(4,5))
# print(arr5)
print(np.arange(1,21,1).reshape(4,5))

# Q6. Perform Element-wise Operations
# Problem:
# Given:
# A = [1, 2, 3, 4]
# B = [10, 20, 30, 40]
# Compute:
# A + B
# A * B
# A²
# Input:
# Two arrays
# Expected Output:
# Three result arrays
# Concepts Required:
# Vectorized operations
print()
arr6 = np.array([1, 2, 3, 4])
arr7 = np.array([10, 20, 30, 40])
print(arr6+arr7)
print(arr6*arr7)
print(arr6**2)

# Q7. Boolean Indexing (Basic)
# Problem:
# From array [5, 12, 7, 18, 3, 25], extract all elements greater than 10.
# Input:
# 1D array
# Expected Output:
# Filtered array
# Concepts Required:
# Boolean indexing
print()
arr8 = np.array([5, 12, 7, 18, 3, 25])
print(arr8[arr8>10])

# Q8. Create Zeros, Ones, Identity
# Problem:
# Create:
# A 3×3 matrix of zeros
# A 2×4 matrix of ones
# A 4×4 identity matrix
# Input:
# Dimensions
# Expected Output:
# Three matrices
# Concepts Required:
# np.zeros(), np.ones(), np.eye()
print()
print(np.zeros((3,3)))
# print(np.zeros_like(((5,5,5),(1,1,1))))
# print(np.zeros_like((5,5,5)))
print(np.ones((2,4)))
# print(np.eye(4,4))
print(np.eye(4))

# Q9. Basic Aggregations
# Problem:
# Given:
# [[2, 4, 6],
#  [1, 3, 5]]
# Find:
# Total sum
# Mean
# Maximum value
# Input:
# 2D array
# Expected Output:
# 3 values
# Concepts Required:
# np.sum(), np.mean(), np.max()
print()
arr9 = np.array([[2, 4, 6],
                [1, 3, 5]])
print(arr9.sum())
print(arr9.mean())
print(arr9.max())

# Q10. Axis-based Sum
# Problem:
# Using the same array:
# [[2, 4, 6],
#  [1, 3, 5]]
# Find:
# Row-wise sum
# Column-wise sum
# Input:
# 2D array
# Expected Output:
# Row sum → [12, 9]
# Column sum → [3, 7, 11]
# Concepts Required:
# Axis operations (axis=0, axis=1)
print()
arr10 = np.array([[2, 4, 6],
                [1, 3, 5]])
print('Row wise sum: ',arr10.sum(axis=1))
print('Cols wise sum: ',arr10.sum(axis=0))
print('-'*20)

# Q11. Advanced Slicing (Submatrix Extraction)
# Problem:
# Given a 5×5 matrix, extract the center 3×3 submatrix.
# Input:
# 5×5 NumPy array
# Expected Output:
# Middle 3×3 matrix
# Concepts Required:
# 2D slicing
print()
arr11 = np.arange(1,26,1).reshape(5,5)
print(arr11)
print(f"\n3X3 Slicing:\n {arr11[1:4,1:4]}")

# Q12. Reverse Array Using NumPy
# Problem:
# Reverse a 1D array without using loops.
# Input:
# [10, 20, 30, 40, 50]
# Expected Output:
# [50, 40, 30, 20, 10]
# Concepts Required:
# Slicing ([::-1])
arr12 = np.arange(10,51,10)
print(arr12[::-1])

# Q13. Replace Using Boolean Condition
# Problem:
# Replace all values less than 10 with -1.
# Input:
# [5, 12, 7, 18, 3, 25]
# Expected Output:
# [-1, 12, -1, 18, -1, 25]
# Concepts Required:
# Boolean indexing + assignment
print()
arr13 = np.array([5, 12, 7, 18, 3, 25])
arr13[arr13 < 10] = -1
print(arr13)

# Q14. Row-wise Maximum
# Problem:
# Find the maximum value of each row in a 2D array.
# Input:
# [[3, 7, 2],
#  [8, 1, 5],
#  [4, 9, 6]]
# Expected Output:
# [7, 8, 9]
# Concepts Required:
# Axis operations (axis=1)
print()
arr14 = np.array([[3, 7, 2],
                [8, 1, 5],
                [4, 9, 6]])
print(arr14.max(axis=1))

# Q15. Column-wise Mean
# Problem:
# Find the mean of each column.
# Input:
# Same as above
# Expected Output:
# Mean of each column
# Concepts Required:
# Axis operations (axis=0)
print()
arr15 = arr14
print(arr15.mean(axis=0))

# Q16. Broadcasting (Scalar)
# Problem:
# Add 5 to every element of a 2D array using broadcasting.
# Input:
# Any 2D array
# Expected Output:
# Updated array
# Concepts Required:
# Broadcasting (scalar)
arr16 = np.array([[1,2],[3,4]])
# arr16 = np.array([1,2])
# print(arr16.shape)
# print(arr16.ndim)
print(arr16 + 5)

# Q17. Broadcasting (Row Addition)
# Problem:
# Add [10, 20, 30] to each row of a 3×3 matrix.
# Input:
# Matrix + 1D array
# Expected Output:
# Row-wise addition
# Concepts Required:
# Broadcasting (1D → 2D)
arr17 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr17_add = [10, 20, 30]
print(arr17 + arr17_add)

# Q18. Normalize a Vector
# Problem:
# Normalize a 1D array using:
# x(norm)=(x−min)/(max−min)​
# Input:
# [10, 20, 30, 40, 50]
# Expected Output:
# Values between 0 and 1
# Concepts Required:
# Min, max, vectorized ops
print()
arr18 = np.array([10, 20, 30, 40, 50])
print(((arr18 - arr18.min())/(arr18.max() - arr18.min())))

# Q19. Find Indices Using Condition
# Problem:
# Find indices of elements greater than 15.
# Input:
# [5, 12, 17, 18, 3, 25]
# Expected Output:
# Indices array
# Concepts Required:
# np.where()
arr19 = np.array([5, 12, 17, 18, 3, 25])
print(np.where(arr19 > 15))

# Q20. Matrix Transpose
# Problem:
# Transpose a 3×2 matrix into 2×3.
# Input:
# [[1, 2],
#  [3, 4],
#  [5, 6]]
# Expected Output:
# [[1, 3, 5],
#  [2, 4, 6]]
# Concepts Required:
# .T or np.transpose()
print()
arr20 = np.array([[1, 2],
                [3, 4],
                [5, 6]])
print(arr20.transpose())

print('-'*20)
# Q21. Filter Rows Based on Condition
# Problem:
# Given a dataset where each row = student and columns = marks in 3 subjects,
# extract only students whose average marks > 60.
# Input:
# [[70, 60, 50],
#  [90, 80, 70],
#  [40, 50, 45],
#  [85, 75, 65]]
# Expected Output:
# Filtered rows (students)
# Concepts Required:
# Mean (axis=1), boolean indexing
print()
arr21 = np.array([[70, 60, 50],
                [90, 80, 70],
                [40, 50, 45],
                [85, 75, 65]])
print(arr21.mean(axis=1))

# Q22. Standardization (Z-score Scaling)
# Problem:
# Standardize a dataset using:
# z=(x−mean)/std
# Input:
# 1D array
# Expected Output:
# Mean ≈ 0, Std ≈ 1
# Concepts Required:
# Mean, std, broadcasting
print()
arr22 = np.array([0.15, 0.15, 0.25, 0.35, 0.45])
mean = arr22.mean()
std = arr22.std()
standardized_arr = (arr22 - mean) / std
print(f"Original Array: {arr22}")
print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")
print(f"Standardized Array: {standardized_arr}")
print(f"\nVerification:")
print(f"New Mean (approx 0): {standardized_arr.mean():.2f}")
print(f"New Std (approx 1): {standardized_arr.std():.2f}")

# Q23. Count Condition Occurrences
# Problem:
# Count how many elements are greater than 50.
# Input:
# Any 2D array
# Expected Output:
# Single integer count
# Concepts Required:
# Boolean condition + np.sum()
print()
arr23 = np.array([[100,20],[312,42]])
arr23 = arr23[arr23 > 50]
count = np.sum(arr23 > 50)
print(len(arr23))
print(count)

# Q24. Replace Entire Column
# Problem:
# Replace the 2nd column of a matrix with [100, 100, 100, ...]
# Input:
# 2D array
# Expected Output:
# Updated matrix
# Concepts Required:
# Column indexing
print()
n1 = np.arange(1,14,4)
# n1 = np.arange(1,14,5) ValueError: cannot reshape array of size 5 into shape (2,2)
arr24 = n1.reshape(2,2)
arr24[:, 1] = 100
print(arr24)

# Q25. Row-wise Normalization
# Problem:
# Normalize each row separately:
# x=x/row_sum
# Input:
# 2D array
# Expected Output:
# Each row sums to 1
# Concepts Required:
# Axis operations + broadcasting
print()
# arr25 = np.arange(1,11,3)
# arr25 = arr25.reshape(2,2)
# # print(arr25)
# print(((arr25)/(arr25.sum(axis=1)+1)))
# print(((arr25)/(arr25[:]+1)))
# Sample 2D array
x = np.array([[1.0, 2.0, 3.0],
                [4.0, 5.0, 6.0]])
# 1. Calculate row sums (shape will be (2,))
row_sums = x.sum(axis=1)
# 2. Divide using broadcasting. 
# keepdims=True ensures row_sums is (2,1) to divide properly.
normalized_x = x / row_sums[:, np.newaxis]
print(normalized_x)
# Output:
# [[0.16666667 0.33333333 0.5       ]
#  [0.26666667 0.33333333 0.4       ]]
# Verification: Each row sums to 1
print(normalized_x.sum(axis=1))
# Output: [1. 1.]

# Q26. Find Row with Maximum Sum
# Problem:
# Identify the row index having the highest total.
# Input:
# 2D array
# Expected Output:
# Row index
# Concepts Required:
# axis=1, np.argmax()
print()
arr26 = np.array([1,2,56,43,42,4,78,3,9])
print(arr26.argmax())

# Q27. Create Masked Dataset
# Problem:
# Set all values < 50 to 0 (without loops).
# Input:
# 2D array
# Expected Output:
# Modified array
# Concepts Required:
# Boolean masking
print()
arr27 = np.array([[54,65,4,6,7,34,54,32,23,12],[43,43,2,3,2,1,123,23,29,40]])
# print(arr27)
arr27[arr27 < 50] = 0
print(arr27)

# Q28. Flatten and Reshape
# Problem:
# Flatten a 3×3 matrix into 1D, then reshape into 1×9.
# Input:
# 3×3 matrix
# Expected Output:
# 1D and reshaped array
# Concepts Required:
# .flatten() / .reshape()
print()
arr28 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr28.flatten())
print(arr28.flatten)
print(arr28.reshape(-1))

# Q29. Dot Product (Matrix × Vector)
# Problem:
# Multiply a 3×3 matrix with a 3-element vector.
# Input:
# Matrix + vector
# Expected Output:
# Resulting vector
# Concepts Required:
# np.dot()
print()
arr29 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr29_ = np.array([12,13,14])
# print(help(np.dot))
print(np.dot(arr29,arr29_))
print(arr29 @ arr29_)

# Q30. Combine Two Datasets (Column-wise)
# Problem:
# Given two arrays of shape (n,1), combine them into (n,2)
# Input:
# A = [[1],[2],[3]]
# B = [[10],[20],[30]]
# Expected Output:
# [[1, 10],
#  [2, 20],
#  [3, 30]]
# Concepts Required:
# np.hstack() / np.concatenate()
print()
arr30_A = np.array([[1],[2],[3]])
arr30_B = np.array([[10],[20],[30]])
# print(np.concatenate((arr30_A,arr30_B),axis=1))
print(np.hstack((arr30_A, arr30_B)))

# Q31. Conditional Row Filtering (Multiple Conditions)
# Problem:
# From a dataset, select rows where:
# Column 1 > 50
# AND Column 2 < 80
# Input:
# 2D array
# Expected Output:
# Filtered rows
# Concepts Required:
# Multiple boolean conditions (&), masking
print()
arr31 = np.array([[200,30,52,49],[100,112,32,4]])
c1 = arr31[:,0] > 50
c2 = arr31[:, 1] < 80
print(arr31[c1 & c2])

# Q32. Clip Values (Range Limiting)
# Problem:
# Limit all values in an array between 10 and 50.
# Input:
# Any array
# Expected Output:
# Values <10 → 10
# Values >50 → 50
# Concepts Required:
# np.clip()
print()
arr32 = np.array([2, 5, 10, 25, 50, 60, 99])
print(f"Original array: {arr32}")
clipped_arr = np.clip(arr32, a_min=10, a_max=50)
print(f"Clipped array:  {clipped_arr}")

# Q33. Row-wise Standardization
# Problem:
# Apply Z-score normalization for each row separately.
# Input:
# 2D array
# Expected Output:
# Each row → mean ≈ 0, std ≈ 1
# Concepts Required:
# Axis operations, broadcasting
print()
arr33 = np.array([[200,30,52,49],[100,112,32,4]])
# mean = arr33.mean(axis=1)
# std = arr33.std(axis=1)
# keepdims=True ensures shapes are (2,1) for correct broadcasting
mean = arr33.mean(axis=1, keepdims=True)
std = arr33.std(axis=1, keepdims=True)
# print(mean, std)
z_score = (arr33 - mean)/std
print(z_score)
print(z_score.mean(axis=1))
print(z_score.std(axis=1))

# Q34. Find Duplicate Values
# Problem:
# Identify duplicate values in a 1D array.
# Input:
# [1, 2, 3, 2, 4, 5, 3, 6]
# Expected Output:
# [2, 3]
# Concepts Required:
# np.unique(), counts
print()
arr34 = np.array([1, 2, 3, 2, 4, 5, 3, 6])
print("Original Value: ",arr34)
print("Unique Value: ",np.unique(arr34))

# Q35. Sort Each Row Independently
# Problem:
# Sort values within each row (not entire matrix).
# Input:
# 2D array
# Expected Output:
# Row-wise sorted matrix
# Concepts Required:
# np.sort(axis=1)
print()
arr35 = np.array([[200,30,52,49],[100,112,32,4]])
print(arr35.sort(axis=1))
# print(help(np.sort))
arr35.sort(axis=1)
print(arr35)

# Q36. Rank Elements (Row-wise)
# Problem:
# Replace each row with ranks (smallest = 1).
# Input:
# 2D array
# Expected Output:
# Row-wise rank matrix
# Concepts Required:
# Sorting + indexing logic
print()
arr36 = np.array([[200,30,52,49],[100,112,32,4]])
print(np.argsort(arr36))
print(np.argsort(arr36)+1)
print(np.argsort(np.argsort(arr36)) + 1)
print(np.argsort(np.argsort(np.argsort(arr36)) + 1))
# np.argsort(np.argsort(arr36)) + 1=[[4 1 3 2]
#                                    [3 4 2 1]]
# Now apply argsort again:
# Row 1: [4,1,3,2]
# Sorted → [1,2,3,4]
# Indices → [1,3,2,0]
# Row 2: [3,4,2,1]
# Sorted → [1,2,3,4]
# Indices → [3,2,0,1]

# Q37. One-Hot Encoding (Manual)
# Problem:
# Convert labels into one-hot encoding.
# Input:
# [0, 1, 2, 1, 0]
# Expected Output:
# [[1,0,0],
#  [0,1,0],
#  [0,0,1],
#  [0,1,0],
#  [1,0,0]]
# Concepts Required:
# Indexing, array creation
print()
arr37 = np.array([0,1,2,1,0])
# arr37 = labels in question
print(f'Raw Data: {arr37}')
print(arr37.max)
print(arr37.max())
print("number of classes: ",arr37.max()+1)
class_num = arr37.max() + 1
print(f"zero matrix:\n {np.zeros((arr37.size, class_num), dtype=int)}")
one_hot = np.zeros((arr37.size, class_num), dtype=int)
one_hot[np.arange(arr37.size), arr37] = 1
print(arr37.size)
print(one_hot)

print()
labels = np.array([[1,1, 0, 2]])
# class_2 = labels.max() + 1
one_hot = np.eye(labels.max())
print(labels.max())
print(one_hot)
one_hot = np.eye(labels.max() + 1)
print(one_hot)
one_hot = np.eye(labels.max() + 1)[labels]
print(one_hot)

# Q38. Matrix Multiplication (Manual Dataset)
# Problem:
# Multiply two matrices using NumPy.
# Input:
# Matrix A (2×3), Matrix B (3×2)
# Expected Output:
# Result (2×2)
# Concepts Required:
# np.dot() / @
print()
mata = np.array([[2,3,4],[4,5,6]])
matb = np.array([[2,3],[4,5],[6,7]])
print(mata)
print(matb)
print("Multiplication is: \n",mata @ matb)

# Q39. Feature Scaling (Min-Max for Each Column)
# Problem:
# Normalize each column independently.
# Input:
# 2D dataset
# Expected Output:
# Each column scaled between 0–1
# Concepts Required:
# Axis operations, broadcasting
print()
arr39 = np.array([[2,3,4],[4,5,6]])
arr39_norm = (arr39 - arr39.min(axis=0)) / (arr39.max(axis=0) - arr39.min(axis=0))
print(arr39_norm)

# Q40. Find Correlation-like Measure
# Problem:
# Given two vectors, compute:
# (∑(x−meanx)(y−meany))/n
# Input:
# Two arrays
# Expected Output:
# Single value
# Concepts Required:
# Mean, vectorized ops, element-wise multiplication
print()
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
mean_x = np.mean(x)
mean_y = np.mean(y)
n = len(x)
cov_measure = np.sum((x - mean_x) * (y - mean_y)) / n
print(cov_measure) 

# Q41. Full Feature Scaling Pipeline
# Problem:
# Given a dataset (rows = samples, cols = features), apply:
# Min-Max scaling
# Then standardization
# Input:
# 2D array
# Expected Output:
# Transformed dataset (same shape)
# Concepts Required:
# Min, max, mean, std, broadcasting, axis
print()
# Input: 2D array (samples, features)
data = np.array([[10, 2, 300], 
                 [20, 4, 100], 
                 [30, 6, 200]], dtype=float)
# 1. Min-Max Scaling: (x - min) / (max - min)
col_min = data.min(axis=0)
print(col_min)
col_max = data.max(axis=0)
print(col_max)
min_max_scaled = (data - col_min) / (col_max - col_min)
print(min_max_scaled)
# 2. Standardization: (x - mean) / std
mean = min_max_scaled.mean(axis=0)
print(mean)
std = min_max_scaled.std(axis=0)
print(std)
transformed_dataset = (min_max_scaled - mean) / std
print(transformed_dataset)

# Q43. Feature-Target Separation
# Problem:
# Last column is target (y), rest are features (X). Separate them.
# Input:
# 2D dataset
# Expected Output:
# X (2D), y (1D)
# Concepts Required:
# Slicing
print()
data = np.array([[10, 2, 300], 
                [20, 4, 100], 
                [30, 6, 200]])
y = data[:,2:3]
x = data[:,:2]
print("Y: \n",y)
print("X: \n",x)
x = data[:,:-1]
y = data[:,-1]
print("Y: \n",y)
print("X: \n",x)
print("y = data[:, -1]: : selects all rows. -1 selects only the last column. This results in a 1D array as requested by the expected output format. x = data[:, :-1]: : selects all rows. :-1 selects all columns except the last one. This results in a 2D array, which is the expected format for features (X).")  

# Q44. Mean Imputation
# Problem:
# Replace all np.nan values with column mean.
# Input:
# 2D array with missing values
# Expected Output:
# Clean dataset
# Concepts Required:
# np.isnan(), mean, axis, broadcasting
print()
# 1. Input: 2D array with missing values
arr = np.array([[1, 2, np.nan],
                [4, np.nan, 6],
                [np.nan, 8, 9]])
# 2. Compute column means, ignoring NaNs (axis=0 for columns)
col_means = np.nanmean(arr, axis=0)
# Output: [2.5, 5.0, 7.5]
# 3. Find indices of NaN values
inds = np.isnan(arr)
# 4. Use broadcasting to replace NaNs with corresponding column means
arr[inds] = np.take(col_means, np.where(inds)[1])
print("Cleaned Dataset:\n", arr)

# Q46. Simple Linear Regression (Single Feature)
# Problem:
# Compute slope (m) and intercept (b) using:
# m= (∑(x−meanx)(y−meany​)​)/∑(x−meanx)^2
# b=meany−m⋅meanx
# Input:
# x (1D), y (1D)
# Expected Output:
# m, b
# Concepts Required:
# Mean, dot-like operations
print()
x = np.array([1,2,3])
y = np.array([4,5,6])
mean_of_x = x.mean()
mean_of_y = y.mean()
num_of_m = sum((x - mean_of_x)*(y - mean_of_y))
# print(num_of_m)
deno = sum((x-mean_of_x)**2)
# print(x-mean_of_x)
# print((x-mean_of_x)**2)
# print(deno)
print(num_of_m/deno)
res = mean_of_y - (deno*mean_of_x)
print(res)
# Q47. Prediction Using Linear Model
# Problem:
# Using m and b, predict y values.
# Input:
# x, m, b
# Expected Output:
# Predicted y
# Concepts Required:
# Vectorized operations
