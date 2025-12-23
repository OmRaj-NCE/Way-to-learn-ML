# 🧠 PART 1: What is a Tuple?
student = ("Raj", 18, "AIML")
/*Tuples are used when:
Data should not be changed
Function returns multiple values
Coordinates, shapes, image sizes
Model weights structure */

# 🔍 PART 2: Tuple Creation
t = (10, 20, 30)
# Single-item tuple (important!):
t = (10,) 

# 📦 PART 3: Accessing Tuple Items
colors = ("red", "green", "blue")
print(colors[0])  
print(colors[-1])  

# ✂️ PART 4: Tuple Slicing
nums = (1, 2, 3, 4, 5)
print(nums[1:4])   # (2,3,4)
print(nums[:3])    # (1,2,3)
print(nums[3:])    # (4,5)

# 🛑 PART 5: Immutability (VERY IMPORTANT)
nums = (1, 2, 3)
nums[1] = 99 

# 🔄 PART 6: Tuple Functions
t = (5, 3, 8, 2)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

# 🧠 PART 7: Tuple Unpacking (VERY Useful)
name, age, dept = ("Raj", 18, "AIML")
print(name)
