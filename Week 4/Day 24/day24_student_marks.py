class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("\nName:", self.name)
        print("Marks:", self.marks)
    def add_bonus(self, bonus):
        self.marks += bonus
        print("Bonus added.")
    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
s1 = Student("Raj", 82)
s1.display()
s1.add_bonus(8)
s1.display()
print("Grade:", s1.get_grade())
