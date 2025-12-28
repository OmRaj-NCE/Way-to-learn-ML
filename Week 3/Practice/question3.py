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
