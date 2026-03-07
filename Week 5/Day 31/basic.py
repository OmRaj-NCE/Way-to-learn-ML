# 📅 DAY 31 — Dictionary & Set Algorithms
# 🎯 Day-31 Objective
# By the end of today you will be able to:
# Use dictionaries to analyze datasets
# Use sets to detect duplicates
# Group data using dictionaries
# Solve real data-cleaning problems
# These skills are used in:
# data preprocessing
# feature engineering
# dataset validation


# 🧠 PART 1 — Duplicate Detection
# Example dataset:
# [4, 7, 2, 4, 9, 7, 1]
# Goal:
# duplicates → [4, 7]
# Algorithm idea:
# 1️⃣ Create empty set
# 2️⃣ Loop through numbers
# 3️⃣ If number already seen → duplicate
# Example
nums = [4, 7, 2, 4, 9, 7, 1]
seen = set()
duplicates = set()
for n in nums:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)
print("Duplicates:", duplicates)


# 🧠 PART 2 — Frequency Ranking
# Example:
data = [1,2,2,3,3,3,4]
# Goal:
# 3 → most frequent
# Algorithm
freq = {}
for n in data:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
        

# 🧠 PART 3 — Grouping Data
# Example dataset:
students = [
("Raj","A"),
("Aman","B"),
("Sita","A")
]
# Goal:
# A → Raj,Sita
# B → Aman
# Example
groups = {}
for name, grade in students:
    if grade not in groups:
        groups[grade] = []
    groups[grade].append(name)
print(groups)
