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

# 6. Word Frequency Counter (Dict + Split)
# Take a sentence from the user.
# Convert it to lowercase → split into words.
# Create a dictionary storing each word and its count.
# Print the dictionary.
data = {}
sentence = input("Enter sentence: ")
words = sentence.lower().split()
for word in words:
    data[word] = data.get(word, 0) + 1
print(data)
data = {}
sentence = "hello world"
# Loop through string -> gets letters: 'h', 'e', 'l', 'l', 'o'...
for char in sentence:
    if char in data:
        data[char] += 1
    else:
        data[char] = 1
print(data)
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# The Long Way (If/Else):
if word in data:
    current_value = data[word] # Get value
else:
    current_value = 0          # Default value
data[word] = current_value + 1
# The Short Way (.get):
data[word] = data.get(word, 0) + 1


# 7. ATM Simulation (While Loop + Conditions)
# Given a starting balance = 1000
# Inside a loop:
# Ask user: deposit, withdraw, or exit
# On deposit: add amount
# On withdraw: check if enough balance
# On exit: print final balance and stop
# Use only loops + variables + if-else.
start_balance = 1000
while True:
  print("1) Deposit\n2) Withdraw\n3) exit")
  a = input("What you want (1/2/3): ")
  if a == "exit" or a == "quit" or a == "3":
    break
  if a == "1":
    b = float(input("Enter amount for deposit: "))
    start_balance += b
    print(f"Your current balance is: {start_balance}")
  if a == "2":
    c = float(input("Enter amount for withdraw: "))
    if c >= start_balance:
        print("Not sufficient Fund")
    else:
        start_balance -= c
    print(f"Your current balance is: {start_balance}")
  if a != "1" or a != "2" or a != "3":
    print("Invalid. Retry")


# 8. Basic JSON File Saver (Dict → JSON)
# Take user input for:
# name
# age
# city
# Store these in a dictionary.
# Save the dictionary into a JSON file named "user_data.json".
# Then read the same file and print the data.
import json
data = {}
count = 0
while True:
    a = input("Enter yes or No: ")
    if a == "No" or a == "no":
        break
    name = input("Enter your name: ")
    city = input("Enter your residance: ")
    age = int(input("Enter your age: "))
    key = f"person{count+1}"
    data[key] = {
        "name": name,
        "age": age,
        "city": city
    }
    count += 1
print(data)
with open("data.json", "w") as f:
    json.dump(data, f)
with open("data.json", "r") as f:
    d = json.load(f)
    print(d)


# Inside a loop, allow user to:
# Add a contact (name + phone)
# Delete a contact
# View all contacts
# Exit
# Use a dictionary to store contacts.
# (Do NOT use functions — only loops and if-else.)
data = {}
while True:
    print("1) Add contact\n2) Delete a contact\n3)View all contact\n4)Exit")
    a = input("1/2/3/4: ")
    if a == "4":
        break
    elif a == "1":
        name = input("Enter name: ")
        contact_add = int(input("Enter contact number: "))
        data[name] = {"Number": contact_add}
        print("Contact added")
    elif a == "2":
        del_contact = input("Enter contact name you want to delete: ")
        if del_contact in data:
            del data[del_contact]  # Use the variable, NOT "name"
            print(f"{del_contact} deleted")
        else:
            print("User not found.")
    elif a == "3":
        if len(data) == 0:  
            print("Enter data first.")
        else:
            print("\n--- Contact List ---")
            for key, val in data.items():
                print(f"{key}: {val['Number']}")


# 10. Pattern + Logic: Word Pyramid
# Take a word from the user, e.g., "PYTHON"
# Print this pattern (using slicing and loops):
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON
word = "PYTHON"
for i in range(1, len(word) + 1):
    print(word[:i])
