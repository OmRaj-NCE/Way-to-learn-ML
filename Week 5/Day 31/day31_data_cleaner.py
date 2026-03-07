data = []
n = int(input("How many numbers? "))
for i in range(n):
    data.append(int(input(f"Enter number {i+1}: ")))
seen = set()
duplicates = set()
for num in data:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
freq = {}
for num in data:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("\nData:", data)
print("Duplicates:", list(duplicates))
print("Frequency:", freq)


# 🧠 THINK LIKE A DATA ENGINEER
# Ask yourself:
# How would I find the most frequent number?
# How would I remove duplicates entirely?
# How would I sort by frequency?
# These questions lead to data analysis and ML features.
