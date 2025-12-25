numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    numbers.append(int(input(f"Enter number {i+1}: ")))

square = lambda x: x * x
is_even = lambda x: x % 2 == 0

squared_numbers = []
even_numbers = []

for num in numbers:
    squared_numbers.append(square(num))
    if is_even(num):
        even_numbers.append(num)

print("\nOriginal:", numbers)
print("Squared:", squared_numbers)
print("Even numbers:", even_numbers)


# When should I avoid lambda?
# ❌ The Nightmare Lambda: Imagine checking if a number is valid (positive, even, and not 100).
check = lambda x: "Valid" if x > 0 and x % 2 == 0 and x != 100 else "Invalid"
# This is hard to read and hard to modify.
#✅ The Clean Function:
def check_number(x):
    if x <= 0:
        return "Invalid"
    if x % 2 != 0:
        return "Invalid"
    if x == 100:
        return "Invalid"
    return "Valid"
