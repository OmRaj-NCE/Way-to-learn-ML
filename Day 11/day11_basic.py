# 🧠 PART 1: What Is a Dictionary?
# A dictionary stores data as key → value pairs.
student = {
    "name": "Raj",
    "age": 18,
    "course": "AIML"
}

# 🔍 PART 2: Accessing Values
print(student["name"])
print(student["age"])
# If key doesn’t exist → error.
# Safer way:
print(student.get("grade", "Not found"))

# 📦 PART 3: Adding & Updating Data
# Add new key
student["grade"] = "A"
# Update existing key
student["age"] = 19

# ❌ PART 4: Removing Data
student.pop("age")
student.popitem()  # removes last added key
del student["course"]

# 🔁 PART 5: Looping Through a Dictionary
# Loop keys
for key in student:
    print(key)
# Loop values
for value in student.values():
    print(value)
# Loop items
for key, value in student.items():
    print(key, value)

# 🧠 PART 6: Nested Dictionary (VERY IMPORTANT)
# Used everywhere:
# JSON
# API response
# ML configs
students = {
    "101": {"name": "Raj", "marks": 85},
    "102": {"name": "Aman", "marks": 90}
}
print(students["101"]["name"])
