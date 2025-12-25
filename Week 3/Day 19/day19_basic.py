# 🧠 PART 1: Why Error Handling Exists
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(a / b)
# If b = 0 ❌ → program crashes.

# ⚠️ PART 2: Common Python Errors (Recognize Them)
# Error	            When it occurs
# ValueError	      Wrong type conversion
# ZeroDivisionError	Divide by zero
# FileNotFoundError	File missing
# KeyError	        Missing dictionary key
# IndexError	      List index out of range

# 🧱 PART 3: Basic try / except
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("Something went wrong!")

# 🎯 PART 4: Catching Specific Errors (BEST PRACTICE)
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# 🔁 PART 5: else Block
# Runs only if no error occurs.
try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    result = x / y
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Result:", result)

# 🧹 PART 6: finally Block
# Runs always, error or not.
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")
#Used for:
#closing files
#releasing resources
#logging

