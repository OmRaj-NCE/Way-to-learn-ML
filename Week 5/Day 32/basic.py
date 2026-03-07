# 📅 DAY 32 — Nested Data Structures & Dataset Logic
# 🎯 Day-32 Objective
# By the end of today you will be able to:
# Work with list of dictionaries
# Analyze multi-field dat
# Extract features from structured datasets
# Build a student dataset analyzer
# This skill directly translates to real dataset processing.


# 🧠 PART 1 — What Real Data Looks Like
# Example dataset:
students = [
    {"name":"Raj","marks":85,"course":"AIML"},
    {"name":"Aman","marks":72,"course":"CSE"},
    {"name":"Sita","marks":91,"course":"AIML"}
]
# Structure:
# List
#  ├─ Dictionary
#  ├─ Dictionary
#  └─ Dictionary
# This is exactly how:
# JSON datasets
# API responses
# ML dataset entries
# look.


# 🧩 PART 2 — Accessing Nested Data
# Example:
print(students[0]["name"])
print(students[2]["marks"])
# Output:
# Raj
# 91


# 🧠 PART 3 — Loop Through Dataset
for s in students:
    print(s["name"], s["marks"])
# Output:
# Raj 85
# Aman 72
# Sita 91


# 🧠 PART 4 — Filtering Dataset
# Example: find students with marks > 80
top_students = []
for s in students:
    if s["marks"] > 80:
        top_students.append(s["name"])
print(top_students)
# Output:
# ['Raj','Sita']


# 🧠 PART 5 — Grouping Dataset
# Goal:
# AIML → Raj,Sita
# CSE → Aman
# Algorithm:
groups = {}
for s in students:
    course = s["course"]
    if course not in groups:
        groups[course] = []
    groups[course].append(s["name"])
