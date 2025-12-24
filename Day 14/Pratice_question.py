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
