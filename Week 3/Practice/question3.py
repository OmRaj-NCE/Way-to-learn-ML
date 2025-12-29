# 11. Password Strength Checker (Functions + Lambda)
# Problem:
# Check password strength.
# Input:
# Password string
# Expected Behavior:
# Length check
# Digit & uppercase check
# Use lambda for validations
# Return strength level

# def check_password_strength(password):
#     score = 0
#     # 1. Check Length
#     if len(password) >= 8:
#         score += 1
#     # 2. Check for Digit
#     # "Is there ANY character in password that is a digit?"
#     if any(char.isdigit() for char in password):
#         score += 1
#     # 3. Check for Uppercase
#     if any(char.isupper() for char in password):
#         score += 1        
#     # 4. Check for Symbol (If it's not just numbers and letters)
#     # The 'not' checks if there is something that ISN'T a letter or number
#     if any(not char.isalnum() for char in password):
#         score += 1
#     # --- Result ---
#     if score == 4:
#         return "💪 Strong"
#     elif score >= 2:
#         return "⚠️ Medium"
#     else:
#         return "❌ Weak"
# # --- Main ---
# user_pass = input("Enter password: ")
# print(f"Strength: {check_password_strength(user_pass)}")

# def check_password_strength(password):
#     score = 0
#     # 1. Check Length
#     if len(password) >= 8:
#         score += 1
#     # 2. Check for Digit (Manual Loop)
#     found_digit = False  # Start by assuming NO
#     for char in password:
#         if char.isdigit():
#             found_digit = True # We found one!
#             break # Stop the loop, we don't need to check the rest
#     if found_digit == True:
#         score += 1
#     # 3. Check for Uppercase (Manual Loop)
#     found_upper = False
#     for char in password:
#         if char.isupper():
#             found_upper = True
#             break
#     if found_upper == True:
#         score += 1
#     # 4. Check for Symbol (Manual Loop)
#     found_symbol = False
#     for char in password:
#         # Check if it is NOT a letter AND NOT a number
#         if not char.isalpha() and not char.isdigit():
#             found_symbol = True
#             break
#     if found_symbol == True:
#         score += 1
#     # --- Final Score ---
#     if score == 4:
#         return "💪 Strong"
#     elif score >= 2:
#         return "⚠️ Medium"
#     else:
#         return "❌ Weak"
# # --- Main ---
# user_pass = input("Enter password: ")
# print(f"Strength: {check_password_strength(user_pass)}")

# The Long Way (What you know):
# found = False
# for char in "Om1":
#     if char.isdigit():
#         found = True
#         break
# print(found)
# The any() Way (The Shortcut):
# # "Is ANY char a digit inside the string 'Om1'?"
# found = any(char.isdigit() for char in "Om1")
# print(found)
def check_password_strength(password):
    """
    Analyzes password and returns its strength level.
    """
    # --- 1. Define Rules using Lambda ---
    # These act like mini-functions that return True/False
    has_length = lambda p: len(p) >= 8
    has_digit  = lambda p: any(char.isdigit() for char in p)
    has_upper  = lambda p: any(char.isupper() for char in p)
    has_symbol = lambda p: any(not char.isalnum() for char in p)
    # --- 2. calculate Score ---
    score = 0
    if has_length(password): score += 1
    if has_digit(password):  score += 1
    if has_upper(password):  score += 1
    if has_symbol(password): score += 1
    # --- 3. Determine Level ---
    if score == 4:
        return "💪 Strong"
    elif score >= 2:
        return "⚠️ Medium"
    else:
        return "❌ Weak"
# --- Main Program ---
print("--- Password Checker ---")
user_pass = input("Enter a password to test: ")
strength = check_password_strength(user_pass)
print(f"Strength Level: {strength}")


# 12. Employee Salary Calculator (*args + **kwargs)
# Problem:
# Calculate total salary.
# Input:
# Base salary
# Allowances (*args)
# Deductions (**kwargs)
# Expected Behavior:
# Calculate net salary
# Display breakdown

# def cal_sal(base_sal, *args, **kwargs):
#     given_sal = base_sal
#     if len(args) > 0:
#         for i in args:
#             given_sal += i
#     if len(kwargs) > 0:
#         print("Deduction display: ")
#     for k,v in kwargs.items():
#         print(f"\t-     {k.capitalize()} : {v}")
#     for ded in kwargs.values():
#         given_sal -= ded
#     print(f"Net salary: {given_sal}")
# cal_sal(123211, 12332,2233, electricity=1222, food=4000, yoga=3000 )
def salary_slip(base_sal, *allowances, **deductions):
    # 1. Calculate Gross (Base + All Allowances) using sum()
    total_allowance = sum(allowances)
    gross_salary = base_sal + total_allowance
    print("\n" + "="*30)
    print(f"💰 Base Salary:    {base_sal}")
    print(f"➕ Allowances:      {total_allowance} (Breakdown: {allowances})")
    print(f"💵 GROSS SALARY:    {gross_salary}")
    print("-" * 30)
    # 2. Process Deductions
    total_deduction = 0
    print("🔻 Deductions:")
    # Loop ONCE for both printing and calculating
    for name, amount in deductions.items():
        print(f"   - {name.capitalize()}: {amount}")
        total_deduction += amount
    print("-" * 30)
    net_salary = gross_salary - total_deduction
    print(f"✅ NET SALARY:      {net_salary}")
    print("="*30 + "\n")
# Calling the function
salary_slip(50000, 2000, 1000, tax=500, pf=1200, insurance=800)

# 13. Student Result System (Nested Functions)
# Problem:
# Generate student result.
# Input:
# Name
# Marks list
# Expected Behavior:
# Calculate total & grade
# Display pass/fail
# Use helper functions
def generate_result(name, marks):
    """
    Main function that controls the logic.
    """
    # --- Nested Helper 1: Calculate Grade ---
    def get_grade(avg):
        if avg >= 90: return "A+ (Outstanding)"
        elif avg >= 80: return "A (Excellent)"
        elif avg >= 70: return "B (Good)"
        elif avg >= 60: return "C (Average)"
        elif avg >= 33: return "D (Pass)"
        else: return "F (Fail)"
    # --- Nested Helper 2: Check Pass/Fail Status ---
    # Rule: Student fails if ANY subject is below 33
    def check_status(marks_list):
        if any(m < 33 for m in marks_list):
            return "FAILED (Failed in one or more subjects)"
        return "PASSED"
    # --- Main Logic ---
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    # We call the nested functions here
    final_grade = get_grade(average_marks)
    status = check_status(marks)
    # If they failed a subject, override the grade to F
    if "FAILED" in status:
        final_grade = "F"
    # --- Display Report Card ---
    print("\n" + "="*30)
    print(f"🎓 STUDENT REPORT: {name.upper()}")
    print("-" * 30)
    print(f"📄 Marks:       {marks}")
    print(f"∑  Total:       {total_marks} / {len(marks)*100}")
    print(f"📊 Average:     {average_marks:.2f}%")
    print("-" * 30)
    print(f"📢 Status:      {status}")
    print(f"🏆 Final Grade: {final_grade}")
    print("="*30)
# --- Test the System ---
# Case 1: Good Student
generate_result("Om Raj", [85, 90, 78, 92, 88])
# Case 2: Student failing one subject (20 marks)
generate_result("Rohan", [50, 60, 20, 55, 65])


# 14. JSON-based User Database
# Problem:
# Store user data persistently.
# Input:
# Name
# Age
# City
# Expected Behavior:
# Save data in JSON file
# Load and display all users
# Handle file errors safely
import json
def save_user_data():
    try:
        # Try loading existing data
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
            print("😍 Congrats! You are the first user")
        # User input
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        city = input("Enter city: ").strip()
        # Store data
        data[name] = {
            "age": age,
            "city": city
        }
        # Save back to JSON
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("\n✅ User data saved successfully!")
        print("📂 Current Database:")
        print(data)
    except ValueError:
        print("❌ Age must be a number")
    except Exception as e:
        print("❌ Something went wrong:", e)
    finally:
        print("🔚 Program finished")
save_user_data()

# 15. Quiz Application
# Problem:
# Create a quiz program.
# Input:
# Questions stored in dictionary
# Expected Behavior:
# Ask questions one by one
# Score calculation using functions
# Final result display
# question = {
#     1:{"What's name of owner":"Om"},
#     2:{"What's his age":str(19)}
#     }
# def quiz():
#     score = 0
#     print("-"*5,"Welcome User","-"*5)
#     for k,v in question.items():
#         for q,ans in v.items():
#             print(f"{k}) {q}")
#             answer = input("What's the answer: ")
#             if ans == answer:
#                 score += 1
#                 print(f"Correct. +1 Score\n{score} is the current Score.")
#             else:
#                 return score
# quiz()
questions = {
    1: {"What's name of owner": "Om"},
    2: {"What's his age": "19"} # Stored directly as string
}
def quiz():
    score = 0
    total_q = len(questions)
    print("-" * 5, "Welcome User", "-" * 5)
    # Loop through the dictionary
    for q_id, q_data in questions.items():
        # q_data is the inner dictionary like {"What's name...": "Om"}
        for question_text, correct_ans in q_data.items():
            print(f"\n{q_id}) {question_text}?")
            user_ans = input("   Your Answer: ").strip() # Remove extra spaces
            # LOGIC FIX: Compare lowercase versions
            if user_ans.lower() == correct_ans.lower():
                score += 1
                print("   ✅ Correct!")
            else:
                print(f"   ❌ Wrong! The answer was '{correct_ans}'")
    # Final Result
    print("\n" + "="*20)
    print(f"🏆 Final Score: {score}/{total_q}")
    if score == total_q:
        print("   Perfect Score! You know Om well.")
    else:
        print("   Better luck next time!")
quiz()
