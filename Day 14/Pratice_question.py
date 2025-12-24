# 1. User Greeting Validator (Beginner)
# Ask the user to enter their name.
# If the name contains only alphabets, print: “Hello, <name>!”
# Otherwise print: “Invalid name!”
# (Hint: use string methods and conditions)
a = input("Enter your first name: ")
b = input("Enter your last name: ")
if a.isalpha() == True and b.isalpha() == True:
  print(f"Hello, <{a} {b}>!")
else:
  print("Invalid name!")


# 2. Basic Shopping Bill Calculator
# Ask the user for the price of 3 items (float).
# Calculate and print the total.
# If total > 500, print “You got a discount!”
# Else print “No discount”.
a = float(input("Enter price of 1st item: "))
b = float(input("Enter price of 2nd item: "))
c = float(input("Enter price of 3rd item: "))
total = sum(a,b,c)
if total > 500:
  print("You got a discount")
else:
  print("No discount")

# 3. Password Strength Checker
# Ask the user to input a password.
# Check the following using conditions and string methods:
# Length ≥ 6
# Contains at least one digit
# Contains at least one uppercase letter
# Print whether the password is Strong or Weak.
password = input("Enter password: ")
has_upper = False
has_digit = False
if len(password) >= 6:
    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
    if has_upper and has_digit:
        print("Strong")
    else:
        print("Weak (Must contain at least one uppercase letter and one digit)")
else:
    print("Weak (Password must be at least 6 characters long)")


# 4. Unique City Collector using Sets
# Take city names from the user in a loop until they type "stop".
# Store them in a set.
# Print how many unique cities they entered.
cities_set = set()
while True:
    cities_input = input("Enter cities name (or type 'quit' to exit): ")
    if cities_input == 'quit':
        break
    else:
        cities_set.add(cities_input)
print(f"{cities_set}. Number of cities entered: {len(cities_set)}")


# 5. Student Score Analyzer (List + Loop)
# You are given a list of marks as input: "45 67 89 23 56"
# Convert this string into a list of integers
# Print the highest and lowest marks
# Print how many marks are above 50
marks_in_str = "45 67 89 23 56"
marks = []
for x in marks_in_str.split():
    marks.append(int(x))
highest = marks[0]
lowest = marks[0]
count = 0
for score in marks:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    if score > 50:
        count += 1
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")
print(f"count : {count}")
