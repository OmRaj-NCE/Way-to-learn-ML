# 🧠 PART 1: What is a String?
name = "Raj"
sentence = "Machine Learning is powerful"

# 🔍 PART 2: Indexing (accessing characters)
name = "Python"
print(name[0])  # P
print(name[5])  # n
print(name[-1])  # n
print(name[-2])  # o

# ✂️ PART 3: Slicing (VERY important)
text = "Machine"
print(text[0:4])   # Mach
print(text[:4])    # Mach
print(text[2:])    # chine
print(text[-3:])   # ine

# 🧰 PART 4: Useful String Functions
s = "   Machine Learning   "
print(s.lower())
print(s.upper())
print(s.strip())
print(s.replace("Machine", "Deep"))
print(s.split())
print(len(s))

# 🔢 PART 5: Looping Over Strings
for ch in "Python":
    print(ch)
