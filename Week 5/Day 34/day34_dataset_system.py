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

# -------- DATA CLEANING --------

clean = []
invalid = []

for s in students:
    if s["marks"] > 100:
        invalid.append(s)
    else:
        clean.append(s)

# -------- AVERAGE MARKS --------

total = 0

for s in clean:
    total += s["marks"]

average = total / len(clean)

# -------- TOP STUDENT --------

top = clean[0]

for s in clean:
    if s["marks"] > top["marks"]:
        top = s

# -------- GROUP BY COURSE --------

groups = {}

for s in clean:
    course = s["course"]

    if course not in groups:
        groups[course] = []

    groups[course].append(s["name"])

# -------- DUPLICATE DETECTION --------

names = set()
duplicates = set()

for s in clean:
    if s["name"] in names:
        duplicates.add(s["name"])
    else:
        names.add(s["name"])

# -------- OUTPUT --------

print("\nClean dataset:", clean)
print("Invalid records:", invalid)
print("Average marks:", average)
print("Top student:", top["name"])

print("\nStudents by course:")
for course, names in groups.items():
    print(course, ":", names)

print("Duplicate names:", list(duplicates))


# 🧠 THINK LIKE A DATA ENGINEER
# Ask yourself:
# How would I export this dataset to JSON?
# How would I sort students by marks?
# How would I find top 3 students?
# These questions lead directly to data science workflows.
