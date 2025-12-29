# 🧠 PART 1: Why __init__ Exists
# Until now:
# class Student:
#     def greet(self):
#         print("Hello")
# Problem:
# Every student is the same
# No name, age, marks stored
# We need a way to initialize data when object is created.
# That’s what __init__ does.

# 🧱 PART 2: What is __init__?
# __init__ is a special method (constructor)
# It runs automatically when an object is created.
# class Student:
#     def __init__(self):
#         print("Student created")
# s1 = Student()   # prints automatically

# 🧠 PART 3: self (VERY IMPORTANT)
# self refers to current object.
# Think:
# self.name → name of THIS student
# self.age → age of THIS student
# Each object has its own self.

# 📦 PART 4: Instance Attributes (REAL DATA)
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# Create objects:
# s1 = Student("Raj", 18)
# s2 = Student("Aman", 20)
# Access data:
# print(s1.name)
# print(s2.age)
# ✔ Same class
# ✔ Different data
# ✔ Separate memory

# 🧠 PART 5: Methods Using Attributes
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def show(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)
