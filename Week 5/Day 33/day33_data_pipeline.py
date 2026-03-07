# Program Requirements
# The program should:
# 1️⃣ Accept numbers
# 2️⃣ Detect outliers (>100)
# 3️⃣ Remove them
# 4️⃣ Compute:
# clean dataset
# average
# normalized values

data = []

n = int(input("How many values? "))

for i in range(n):
    data.append(int(input(f"Enter value {i+1}: ")))

clean = []
outliers = []

for num in data:
    if num > 100:
        outliers.append(num)
    else:
        clean.append(num)

total = 0

for num in clean:
    total += num

average = total / len(clean)

normalized = []

max_val = max(clean)

for num in clean:
    normalized.append(num / max_val)

print("\nOriginal data:", data)
print("Outliers:", outliers)
print("Clean data:", clean)
print("Average:", average)
print("Normalized values:", normalized)

# 🧠 THINK LIKE A DATA ENGINEER
# Ask yourself:
# How would I detect negative values?
# How would I remove duplicates first?
# How would I scale values between 0-1?
# These lead directly to feature engineering.
