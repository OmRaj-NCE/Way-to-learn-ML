# Program Requirements
# The program should:
# Accept student records
# Store them in list of dictionaries
# Print:
# all students
# average marks
# top student
# students grouped by course

students = []

n = int(input("How many students? "))

for i in range(n):
    name = input("Name: ")
    marks = int(input("Marks: "))
    course = input("Course: ")

    students.append({
        "name": name,
        "marks": marks,
        "course": course
    })

total = 0
top_student = students[0]

groups = {}

for s in students:
    total += s["marks"]

    if s["marks"] > top_student["marks"]:
        top_student = s

    course = s["course"]

    if course not in groups:
        groups[course] = []

    groups[course].append(s["name"])

average = total / len(students)

print("\nStudents:", students)
print("Average marks:", average)
print("Top student:", top_student["name"])

print("\nStudents by course:")
for course, names in groups.items():
    print(course, ":", names)


# 🧠 THINK LIKE A DATA ENGINEER
# Ask yourself:
# How would I sort students by marks?
# How would I find top 3 students?
# How would I export this dataset to JSON?
# These are real ML preprocessing questions.
