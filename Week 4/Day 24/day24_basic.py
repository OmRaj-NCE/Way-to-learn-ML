📅 DAY 24 — Methods, self, and Object Behavior

# 🧠 PART 1: Function vs Method (CRITICAL)
# Function (independent)
# def add(a, b):
#     return a + b
# Method (belongs to a class)
# class Test:
#     def add(self, a, b):
#         return a + b
# Call difference:
# add(2, 3)          # function
# obj.add(2, 3)      # method

# 🧠 PART 2: self Revisited (Deep Understanding)
# self means:
# “This object’s data”
# Example:
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def show(self):
#         print(self.name, self.marks)
# self.name → name of THIS student
# self.marks → marks of THIS student

# 🔄 PART 3: Updating Object State (VERY IMPORTANT)
# Objects are not static.
# Their data can change.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def add_marks(self, extra):
#         self.marks += extra

# 🧪 PART 4: Multiple Methods Working Together
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def add_marks(self, extra):
#         self.marks += extra
#     def grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         else:
#             return "C"
