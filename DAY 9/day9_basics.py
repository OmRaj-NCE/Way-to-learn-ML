# 🧠 PART 1: What is a List?
numbers = [10, 20, 30, 40]
names = ["Raj", "Aman", "Sita"]
mixed = [10, "Raj", 3.14, True]

# 📦 PART 2: Accessing Items (Indexing)
fruits = ["apple", "banana", "mango"]
print(fruits[0])   # apple
print(fruits[2])   # mango
print(fruits[-1])  # mango
print(fruits[-2])  # banana

# ✂️ PART 3: List Slicing
nums = [1, 2, 3, 4, 5]
print(nums[0:3])   # [1,2,3]
print(nums[2:])    # [3,4,5]
print(nums[:4])    # [1,2,3,4]

# 🛠️ PART 4: Modifying Lists (Mutable)
# Changing values
nums = [10, 20, 30]
nums[1] = 99
print(nums) 
# Adding items
nums.append(40)
nums.insert(1, 15)
# Removing items
nums.remove(30)
nums.pop()        # removes last
nums.pop(1)       # removes index 1

# 🔍 PART 5: Useful List Functions
nums = [5, 1, 10, 2]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
nums.sort()
nums.reverse()

# 🔁 PART 6: Looping Through Lists
fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)
