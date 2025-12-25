# 1. Smart Calculator (Function Basics)
# Problem:
# Create a calculator program using functions.
# Input:
# Two numbers
# Operator (+, -, *, /)
# Expected Behavior:
# Use separate functions for each operation
# Handle division by zero using try-except
# Print result or meaningful error message
def cal(a=0,b=0,op=""):
    a = float(input("Enter 1st num: "))
    b = float(input("Enter 2nd num: "))
    op = input("Enter operator (+ - * /): ")
    try:
        if op == "+":
            add = print(a+b)
            return add
        elif op == "-":
            sub = print(a-b)
            return sub
        elif op == "*":
            mul = print(a*b)
            return mul
        else:
            div = print(a/b)
            return div
    except ValueError:
        print("Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print("Error:", e)
cal()



# 2. User Registration Validator
# Problem:
# Validate user input using functions.
# Input:
# Name
# Age
# Email
# Expected Behavior:
# Name must not be empty
# Age must be numeric
# Email must contain @
# Return validation status from functions
def validate_name(name):
    """Returns True if name is not empty."""
    return len(name.strip()) > 0
def validate_age(age_input):
    """Returns True if age is a valid number."""
    return age_input.isdigit()
def validate_email(email):
    """Returns True if email contains '@'."""
    return "@" in email
print("--- User Sign Up ---")
user_name = input("Enter Name: ")
user_age = input("Enter Age: ")
user_email = input("Enter Email: ")
is_name_ok = validate_name(user_name)
is_age_ok = validate_age(user_age)
is_email_ok = validate_email(user_email)
if is_name_ok and is_age_ok and is_email_ok:
    print("\n✅ Success: All inputs are valid!")
    print(f"User: {user_name}, Age: {user_age}, Email: {user_email}")
else:
    print("\n❌ Validation Failed:")
    if not is_name_ok:
        print("- Name cannot be empty.")
    if not is_age_ok:
        print("- Age must be a number.")
    if not is_email_ok:
        print("- Email must contain '@'.")
# data = []
# while True:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     email = input('Enter your email: ')
#     try:
#         try:
#             if name != "" and name.isaplha() ==  True:
#                 data.append(name)
#             else:
#                 print("Enter a valid name first without space.")
#                 break
#             if age >= 5 and age <= 80:
#                 data.append(age)
#             else:
#                 print("Age must be between 5 and 80")
#                 break
#             if "@" in email or "@gmail.com" in email:
#                 print("Email stored")
#         except ValueError:
#             print("Invalid input!")
#         else:
#             print("Input is valid:", name or age or email)
#     except Exception as e:
#         print("Error:", e)
#     finally:
#         print("Thank you")
# print(data)
data = []
while True:
    print("\n--- New Entry ---")
    # 1. Start TRY block immediately
    try:
        # Ask inputs inside the safety zone
        name = input("Enter your name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        age_input = input("Enter your age: ") # Keep as string first
        email = input('Enter your email: ')
        # --- VALIDATION LOGIC ---
        # Check Name (isalpha fails on spaces, so we check if it's not empty)
        if not name.isalpha():
            # Raise a custom error to jump to 'except'
            raise ValueError("Name must only contain letters (no numbers/symbols).")
        # Check Age (Convert to int here)
        age = int(age_input) 
        if not (5 <= age <= 80):
            raise ValueError("Age must be between 5 and 80.")
        # Check Email
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        # --- SUCCESS ---
        # Only if we get here, the data is safe to add
        # Storing as a Dictionary is much better than a flat list!
        person = {
            "name": name, 
            "age": age, 
            "email": email
        }
        data.append(person)
        print("✅ Data Saved Successfully!")
    # 2. Catch ALL input errors here
    except ValueError as e:
        # This catches 'int()' failures AND our custom 'raise ValueError' messages
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
    finally:
        print("Ready for next step...")
print("\nFinal Data:", data)

# 3. Shopping Bill Generator (*args)
# Problem:
# Create a function that calculates total bill.
# Input:
# Any number of item prices using *args
# Expected Behavior:
# Return total amount
# Apply 10% discount if total > 1000
# Print final bill
def cal_bill(*args):
    a = sum(args)
    print(f"Your total bill before discount: {a}")
    if a > 1000:
        b = (0.1 * a)
        a -= b
    c = print(f"Your total bill after discount: {a}")
    return c
cal_bill(200,600,300)

# 4. Student Marks Analyzer (Multiple Returns)
# Problem:
# Analyze marks of a student.
# Input:
# List of marks
# Expected Behavior:
# Function returns: total, average, highest, lowest
# Display all values clearly

# def analyze_marks(marks_list):
#     total_marks = sum(marks_list)
#     if len(marks_list) > 0:
#         average_marks = total_marks / len(marks_list)
#         highest_mark = max(marks_list)
#         lowest_mark = min(marks_list)
#     else:
#         average_marks = 0
#         highest_mark = 0
#         lowest_mark = 0
#     return total_marks, average_marks, highest_mark, lowest_mark
# student_marks = [78, 92, 45, 88, 63]
# tot, avg, high, low = analyze_marks(student_marks)
# print("--- Student Analysis ---")
# print(f"Total Score: {tot}")
# print(f"Average:     {avg:.2f}")
# print(f"Highest:     {high}")
# print(f"Lowest:      {low}")
def analyze_marks(marks_list):
    total = sum(marks_list)
    if len(marks_list) > 0:
        avg = total / len(marks_list)
        high = max(marks_list)
        low = min(marks_list)
    else:
        avg, high, low = 0, 0, 0
    return total, avg, high, low
class_data = {
    "Om":    [78, 92, 45, 88, 63],
    "Rahul": [55, 60, 58, 62, 59],
    "Priya": [98, 95, 99, 92, 97]
}
print(f"{'Name':<10} {'Total':<8} {'Avg':<8} {'High':<6} {'Low':<6}")
print("-" * 40)
for name, marks in class_data.items():
    tot, avg, high, low = analyze_marks(marks)
    print(f"{name:<10} {tot:<8} {avg:<8.1f} {high:<6} {low:<6}")

