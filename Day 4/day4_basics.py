# 🧠 PART 1: Boolean Logic
True
False

# 🔗 PART 2: Logical Operators
age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible to vote")

marks = 35
if marks >= 40 or marks == 39:
    print("Allowed")

logged_in = False
if not logged_in:
    print("Please login")

# 🧱 PART 4: Nested if
age = 20
if age >= 18:
    if age <= 60:
        print("Working age")
    else:
        print("Senior citizen")
else:
    print("Minor")
