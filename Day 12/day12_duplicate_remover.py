data = []
n = int(input("How many values? "))
for i in range(n):
    value = input(f"Enter value {i+1}: ")
    data.append(value)
unique_values = set(data)
print("\nOriginal List:", data)
print("Unique Values:", unique_values)
print("Total Unique:", len(unique_values))

# Ask yourself:
# Why does ML preprocessing remove duplicates?
# How are unique tokens stored in NLP?
# Why are sets faster than lists for membership checking?

# Input: ["apple", "banana", "apple", "orange", "banana"]
#Set Operation: set(Input) $\rightarrow$ {"apple", "banana", "orange"}
# Result: The "Vocabulary" is size 3.

# This is the most important concept for optimizing code.The List Way (The Librarian Walk):If I ask, "Is the book Harry Potter in this library (List)?", you have to walk down every aisle and check every single book one by one until you find it. If the library has 1 million books, this takes a long time.Math: $O(N)$ (Linear Time).The Set Way (The Computer Teleport):Sets use a Hash Function. When you put Harry Potter in a set, the computer runs a math formula: hash("Harry Potter") = Shelf 42.When you ask, "Is Harry Potter in the set?", the computer runs the math again: hash("Harry Potter") = Shelf 42. It teleports directly to Shelf 42 to check. It doesn't care if there are 10 books or 10 billion books; it takes 1 step.Math: $O(1)$ (Constant Time).
