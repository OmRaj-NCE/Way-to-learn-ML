# 📅 DAY 16 — Function Arguments (Default & Keyword)
# 🧠 PART 1: Recap — Positional Arguments
def greet(name, age):
    print("Name:", name)
    print("Age:", age)
greet("Raj", 18)

# 🎯 PART 2: Default Arguments (VERY IMPORTANT)
def greet(name, country="India"):
    print("Name:", name)
    print("Country:", country)

greet("Raj")
greet("Aman", "USA")

# ⚠️ Default Argument Rule (INTERVIEW IMPORTANT)
# ❌ Wrong:
def test(a=10, b):
    pass
# ✔ Correct:
def test(a, b=10):
    pass
# 👉 Default arguments must be at the end.

# 🧾 PART 3: Keyword Arguments
# You can pass values by parameter name.
def student(name, age, grade):
    print(name, age, grade)
student(age=18, grade="A", name="Raj")

# 🔀 PART 4: Mixing Positional + Keyword Arguments
def info(name, age, city="Patna"):
    print(name, age, city)
info("Raj", 18)
info("Aman", age=20, city="Delhi")
# ⚠️ Rule:
# Positional arguments → first
# Keyword arguments → after

# 🧠 Why This Is HUGE for ML
# ML code looks like this:
model = train_model(
    data=train_data,
    epochs=10,
    lr=0.01,
    optimizer="adam"
)
