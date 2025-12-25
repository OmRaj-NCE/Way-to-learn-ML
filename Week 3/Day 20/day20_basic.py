# 📅 DAY 20 — MODULES & IMPORTS
# 🧠 PART 1: What Is a Module?
# A module is simply a Python file (.py) that contains reusable code.
# Examples:
# math.py → math functions
# json.py → JSON handling
# random.py → randomness
# You’ve already used modules without realizing:
# import json

# 📦 PART 2: Importing Modules (3 Ways)
# 1️⃣ Import whole module
import math
print(math.sqrt(16))
# 2️⃣ Import specific functions
from math import sqrt, pow
print(sqrt(25))
# 3️⃣ Import with alias
import math as m
print(m.sqrt(36))
# ✔ Alias is common in ML (import numpy as np later)

#🧱 PART 3: Creating Your Own Module (IMPORTANT)
# Step 1: Create a file
# utils.py
# Step 2: Write reusable functions
def add(a, b):
    return a + b
def is_even(n):
    return n % 2 == 0
# 🔁 PART 4: Using Your Module
# Create another file:
# main.py
import utils
print(utils.add(10, 5))
print(utils.is_even(10))

# ⚠️ PART 5: __name__ == "__main__" (INTRO)
def greet():
    print("Hello")
if __name__ == "__main__":
    greet()
# Meaning:
# Runs only when file is executed directly
# Does NOT run when imported
# This is used heavily in:
# ML training scripts
# APIs
# pipelines
# (We’ll go deeper later.)

