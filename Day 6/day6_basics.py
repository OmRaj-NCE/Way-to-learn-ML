/* 🧠 PART 1: Why for Loop Exists
while loop → repeat until condition fails
for loop → repeat for each item in a sequence*/

# 🔁 PART 2: Basic for Loop
for i in range(1, 6):
    print(i)
# range(start, stop, step)

# 🔢 PART 4: Loop with Calculations
total = 0
for i in range(1, 6):
    total += i
print(total)

# 🛠️ PART 5: MINI-PROJECT — Multiplication Table
# day6_table.py
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

/*🔄 PART 6: break & continue in for Loop
break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)*/
