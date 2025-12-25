# 🧠 PART 1: What Is a Lambda Function?
def add(a, b):
    return a + b
# Lambda version:
add = lambda a, b: a + b

# ✍️ PART 2: Lambda Syntax (MEMORIZE)
# lambda arguments: expression

# 🧪 PART 3: Simple Lambda Examples
square = lambda x: x * x
print(square(5))
is_even = lambda x: x % 2 == 0
print(is_even(10))

# 🔀 PART 4: Lambda with Conditional Expression
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))
