print("Safe Calculator")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Calculator execution completed.")


# What could fail in my program?
# Did I handle user mistakes?
# Will this crash in production?

#Scenario A: The "Typo" Crash
#Prompt: How many numbers?
#User types: "five" (or "10 " with a space, or "3.5")
#Result: ValueError: invalid literal for int() with base 10: 'five'
#Outcome: The program stops immediately.
#Scenario B: The "Empty" Crash
#Prompt: Enter number 1:
#User hits: Enter (accidentally)
#Result: ValueError (Cannot convert empty string to int).
#Outcome: Crash.
#Scenario C: The "Negative List" Bug
#Prompt: How many numbers?
#User types: -5
#Result: No crash, but the loop range(-5) runs 0 times. The program prints empty lists and ends instantly. This is a Logic Error.


 
