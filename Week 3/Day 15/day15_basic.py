# 🧠 PART 1: What Is a Function?
print("Hello")
print("Hello")
print("Hello")
def greet():
    print("Hello")
greet()
greet()
greet()

# ✍️ PART 2: Function Syntax
def function_name():
    # code
def welcome():
    print("Welcome future ML engineer!")
welcome()

# 📥 PART 3: Function With Parameters
def greet(name):
    print("Hello", name)
greet("Raj")

# 📤 PART 4: Function With Return Value
def add(a, b):
    return a + b
result = add(5, 3)
print(result)

# 🎛 PART 5: Multiple Returns
def stats(a, b):
    return a + b, a - b
sum_, diff = stats(10, 5)
print(sum_, diff)
