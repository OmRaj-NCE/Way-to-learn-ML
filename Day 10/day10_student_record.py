# Why tuple?
# Because student record should not be modified accidentally.
student = ()
name = input("Enter student name: ")
age = int(input("Enter age: "))
grade = input("Enter grade: ")
student = (name, age, grade)
print("\nStudent Record:")
print("Name:", student[0])
print("Age:", student[1])
print("Grade:", student[2])
print("\nRecord stored safely as tuple (immutable).")


# 🧠 THINK LIKE AN ENGINEER
# Ask yourself:
# When do I need immutability?
# Why do ML libraries store shapes as tuples?
# How do tuples prevent accidental bugs?

# In AI/ML, the "shape" of a tensor (e.g., a $1920 \times 1080$ image) is fundamental structural data.
/*3. How do Tuples prevent accidental bugs?
Imagine you are writing a physics simulation for your exam notes. You have a constant for gravity and position.

# BAD (List): Mutable
constants = [9.8, 0, 0] 
# ... 1000 lines of code ...
constants[0] = 1.62 # Oops! Someone changed Earth gravity to Moon gravity by mistake.
# Result: Your entire simulation breaks silently.

# GOOD (Tuple): Immutable
constants = (9.8, 0, 0)
# ... 1000 lines of code ...
constants[0] = 1.62*/
