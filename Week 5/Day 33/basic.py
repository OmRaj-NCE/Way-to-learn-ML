# 📅 DAY 33 — Real Data Processing Utilities
# 🎯 Day-33 Objective
# By the end of today you will be able to:
# Build multi-step data pipelines
# Detect outliers
# Filter datasets using conditions
# Transform and clean data
# Design data preprocessing workflows
# These are the exact steps used before machine learning training.


# 🧠 PART 1 — What Data Pipelines Do
# Typical pipeline:
# Raw data
#    ↓
# Remove invalid values
#    ↓
# Remove outliers
#    ↓
# Transform data
#    ↓
# Compute statistics
#    ↓
# Ready dataset
# You will implement a small version of this today.


# 🧩 PART 2 — Outlier Detection Concept
# Example dataset:
data = [10, 12, 11, 9, 13, 200]
# Clearly 200 is an outlier.
# Simple rule (for today):
# If number > 100 → treat as outlier


# 🧠 PART 3 — Filtering Data
# Algorithm:
# 1️⃣ Read numbers
# 2️⃣ Detect invalid values
# 3️⃣ Detect outliers
# 4️⃣ Keep clean data
# Example:
clean = []
for n in data:
    if n <= 100:
        clean.append(n)
        
        
# 🧠 PART 4 — Data Transformation
# Example transformation:
# Normalize values
# Simple version today:
# divide all numbers by max value
# Example:
normalized = []
for n in clean:
    normalized.append(n / max(clean))
