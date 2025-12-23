# 🧠 PART 1: What Is a Nested Loop?
for i in range(3):
    for j in range(3):
        print(i, j)

# ⭐ PART 3: Pattern Printing (Logic Builder)
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
# Pattern 2: Right Triangle
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 3: Number Triangle
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
