# 🧠 PART 1: Why Loops Exist
print("Hello")
print("Hello")
print("Hello")

i = 1
while i <= 3:
    print("Hello")
    i += 1

# 🔄 PART 2: while Loop Syntax
i = 1
while i <= 5:
    print(i)
    i += 1
<--How it works
Check condition
Run block
Update variable
Repeat -->

# ⚠️ PART 3: Infinite Loop (DANGEROUS)
i = 1
while i <= 5:
    print(i)

# ⛔ PART 4: break Statement
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

# ⏭️ PART 5: continue Statement
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
