# 🧠 PART 1: Why *args and **kwargs Exist
# Problem without them:
def add(a, b, c, d):
    return a + b + c + d
# What if inputs change? ❌
# This is not scalable.

# ⭐ PART 2: *args (Multiple Positional Arguments)
# *args collects extra positional arguments into a tuple.
def add(*args):
    print(args)
add(1, 2, 3, 4)
# 🧮 Example: Sum Any Number of Values
def total_sum(*nums):
    total = 0
    for n in nums:
        total += n
    return total
print(total_sum(1, 2))
print(total_sum(1, 2, 3, 4, 5))
# 🧠 Important Rule
# *args → tuple
# Name can be anything, but args is standard

# ⭐ PART 3: **kwargs (Multiple Keyword Arguments)
# **kwargs collects named arguments into a dictionary.
def show_info(**kwargs):
    print(kwargs)
show_info(name="Raj", age=18, city="Patna")

# 🔁 Looping Through **kwargs
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
