import numpy as np
data = []
n = int(input("How many students? "))
for i in range(n):
    study = int(input("Hours studied: "))
    sleep = int(input("Sleep hours: "))
    data.append([study, sleep])
X = np.array(data)
print("\nRaw Data:\n", X)

# -------- STEP 1: NORMALIZATION --------
X_norm = X / X.max(axis=0)
print("\nNormalized Data:\n", X_norm)

# -------- STEP 2: MODEL WEIGHTS --------
# importance of features
weights = np.array([0.7, 0.3])

# -------- STEP 3: PREDICTION --------
scores = np.dot(X_norm, weights)
print("\nPerformance Scores:\n", scores)

# -------- STEP 4: CLASSIFICATION --------
result = []
for s in scores:
    if s > 0.7:
        result.append("High Performer")
    elif s > 0.4:
        result.append("Average")
    else:
        result.append("Low Performer")
print("\nResults:")
for i in range(n):
    print(f"Student {i+1}:", result[i])
