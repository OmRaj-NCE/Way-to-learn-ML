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
