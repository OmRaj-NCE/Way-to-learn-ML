# 📅 DAY 34 — Dataset Processing System (Mini Project)
# 🎯 Day-34 Objective
# By the end of today you will:
# Build a complete dataset processor
# Combine lists + dictionaries + sets
# Perform cleaning, filtering, statistics
# Design a multi-step data pipeline
# Write code that resembles real data engineering tasks


# 🧠 PART 1 — System Idea
# We will create a program that processes a student dataset.
# Each record contains:
# name
# marks
# course
# Example dataset:
students = [
    {"name":"Raj","marks":85,"course":"AIML"},
    {"name":"Aman","marks":72,"course":"CSE"},
    {"name":"Sita","marks":91,"course":"AIML"}
]


# 🧠 PART 2 — Pipeline Steps
# The system should perform:
# Input dataset
#      ↓
# Remove invalid marks (>100)
#      ↓
# Compute average marks
#      ↓
# Find top student
#      ↓
# Group students by course
#      ↓
# Detect duplicate names
# This mimics real dataset validation pipelines.
