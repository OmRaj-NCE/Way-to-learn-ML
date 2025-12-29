class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def display(self):
        print("\n--- STUDENT PROFILE ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
s1 = Student("Raj", 18, "AIML")
s2 = Student("Aman", 20, "CSE")
s1.display()
s2.display()

