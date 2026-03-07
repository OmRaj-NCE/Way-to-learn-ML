nums = []

n = int(input("How many numbers? "))

for i in range(n):
    nums.append(int(input(f"Enter number {i+1}: ")))

largest = nums[0]
smallest = nums[0]
total = 0
evens = []

for num in nums:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    total += num

    if num % 2 == 0:
        evens.append(num)

average = total / len(nums)

print("\nNumbers:", nums)
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even numbers:", evens)


# 🧠 THINK LIKE AN ENGINEER
# Ask yourself:
# How would I remove duplicates?
# How would I sort numbers manually?
# How would I detect outliers?
# This thinking builds algorithmic intuition.
