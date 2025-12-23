nums = []
n = int(input("How many numbers? "))
for i in range(n):
    value = int(input(f"Enter number {i+1}: "))
    nums.append(value)
print("\nYour list:", nums)
print("Largest:", max(nums))
print("Smallest:", min(nums))
print("Sum:", sum(nums))
print("Average:", sum(nums) / len(nums))

# How would I store marks of students?
# What if I need top 3 numbers?
# How do ML datasets look internally?

# 1. Create one main list to hold everything
all_students = [] 
while True:
    enter = input("Type 'quit' to exit, or press Enter to add a student: ")
    if enter.strip().lower() == "quit":
        break
    # 2. Get the inputs
    student_name = input("Enter the student's name: ")
    mark = input("Enter marks: ")
    # 3. Create a "mini-list" for this one student
    # Index 0 is the Name, Index 1 is the Mark
    current_student = [student_name, mark]
    # 4. Add that mini-list to the main list
    all_students.append(current_student)
print("\n--- Final List ---")
print(all_students) 
# Example of how to print it neatly:
for student in all_students:
    # student[0] is the name, student[1] is the mark
    print("Name:", student[0], "| Marks:", student[1])


all_students.sort(reverse=True)
top_3 = all_students[:3]
print("\n--- Top 3 Students ---")
for student in top_3:
    # student[0] is now Mark, student[1] is Name
    print(f"{student[1]} scored {student[0]}")
