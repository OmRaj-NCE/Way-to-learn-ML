# 🧠 PART 1: What Is a Set?
# A set is:
# Unordered
# Unindexed
# Contains only unique values
# Very fast for membership checking
s = {1, 2, 3, 4}
print(s)   
s = {1, 2, 2, 3}
print(s)    # {1, 2, 3}

# 📌 PART 2: Creating a Set
nums = {10, 20, 30}
# From a list:
l = [1, 2, 2, 3, 3, 4]
s = set(l)
# Empty set (IMPORTANT):
s = set()   # NOT {}
# {} creates a dictionary, not a set.

# 🧰 PART 3: Adding & Removing Values
s.add(50)
s.remove(20)   # error if not exists
s.discard(20)  # safe remove
s.pop()        # removes random item

# 🔎 PART 4: Membership Test (Super Fast)
if 10 in s:
    print("Found")
# This is used heavily in:
# checking if a token exists
# checking if a feature is present
# removing duplicates in datasets

# 🧮 PART 5: Set Operations (VERY IMPORTANT)
# Union (combine unique values)
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)     # {1,2,3,4,5}
# Intersection (common values)
print(a & b)     # {3}
# Difference (only in a)
print(a - b)     # {1,2}
# Symmetric Difference (not common)
print(a ^ b)     # {1,2,4,5}
# These operations are used in ML to:
# compare vocabularies
# match features
# remove overlaps
# find missing elements
