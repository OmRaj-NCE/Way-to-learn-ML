import numpy as np

data = []

n = int(input("How many samples? "))

for i in range(n):
    x1 = int(input("Feature 1: "))
    x2 = int(input("Feature 2: "))
    data.append([x1, x2])

X = np.array(data)

# weights
W = np.array([2, 3])

# prediction
y = np.dot(X, W)

print("\nDataset:\n", X)
print("Weights:", W)
print("\nPredictions:", y)
