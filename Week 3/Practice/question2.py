# 6. Contact Book using **kwargs
# Problem:
# Store contact details dynamically.
# Input:
# Name
# Any number of details (phone, email, city…)
# Expected Behavior:
# Function accepts **kwargs
# Stores and prints contact info neatly
# print("--------------------Contact Book Opened---------------")
# data = {}
# while True:
#     action = input("\n1) Contact Info\n2) Add Contact\nEnter 1 or 2: ")
#     # --- VIEW CONTACTS ---
#     if action == "1" or action.lower() == "contact":
#         if len(data) == 0:
#             print("⚠️ Book is empty.")
#         else:
#             print("\n--- Saved Contacts ---")
#             # Loop 1: Go through each person
#             for contact_name, details in data.items():
#                 print(f"👤 {contact_name}")  # Print name ONCE
                
#                 # Loop 2: Go through their details
#                 for label, info in details.items():
#                     # \t adds a "tab" space for indentation
#                     print(f"\t- {label.capitalize()}: {info}")
                
#                 print("-" * 20) # Divider line between people
#     # --- ADD CONTACT ---
#     elif action == "2" or action.lower() == "add contact":
#         name = input("Enter name: ")
#         if len(name) < 1:
#             print("❌ Name must be greater than 1 char.")
#             continue # Restart loop (Don't close program!)
#         phone = input("Enter contact No.: ")
#         if len(phone) != 10:
#             print("❌ Phone must be 10 digits.")
#             continue
#         print("✅ Basic info valid.")
#         # FIX 1: Initialize optional variables with a default value first
#         email = "Not Provided"
#         city = "Not Provided"
#         # --- OPTIONAL EMAIL ---
#         action_email = input("Want to fill email? (yes/no): ")
#         if action_email.lower() == "yes" or action_email.lower() == "email":
#             email_input = input("Enter email: ")
#             # Logic Fix: Use 'or' to check if EITHER is missing
#             if "@" not in email_input or ".com" not in email_input:
#                 print("❌ Invalid email format (skipped).")
#             else:
#                 email = email_input # Only update if valid
#                 print("Email Saved")
#         # Note: We removed the 'else: continue' so the code keeps flowing down!
#         # --- OPTIONAL CITY ---
#         action_city = input("Want to fill city? (yes/no): ")
#         if action_city.lower() == "yes" or action_city.lower() == "city":
#             city_input = input("Enter city: ")
#             if len(city_input) < 2:
#                 print("❌ Invalid city (skipped).")
#             else:
#                 city = city_input
#                 print("City Entered")
#         # FIX 2: Now this always works because 'email' and 'city' exist!
#         data[name] = {
#             "phone": int(phone), # Safe to convert now
#             "email": email,
#             "city": city
#         }
#         print(f"✅ Info saved for {name}!")

# 1. The Function with **kwargs
# This function doesn't care if you send email, city, age, or hobby.
# It just saves whatever you give it.
def save_contact(book, name, **details):
    book[name] = details
    print(f"\n✅ Contact '{name}' saved with details:")
    for key, value in details.items():
        print(f"   - {key.capitalize()}: {value}")
# --- Main Program ---
data = {}
print("--- Dynamic Contact Book ---")
while True:
    action = input("\n1) View Contacts\n2) Add Contact\n3) Exit\nChoose: ")
    if action == "3":
        break
    elif action == "1":
        if not data:
            print("⚠️\tBook is empty.")
        else:
            print()
            for name, details in data.items():
                print(f"👤 {name}: {details}")
    elif action == "2":
        # Required Inputs
        name = input("Enter Name: ")
        phone_str = input("Enter Phone: ")
        # Validation Logic
        if len(name) < 2:
            print("❌ Name too short.")
            continue # Skip to next loop, don't break!
        if len(phone_str) != 10:
            print("❌ Phone must be 10 digits.")
            continue
        # Initialize dynamic details with the required phone number
        current_details = {"phone": int(phone_str)}
        # --- DYNAMIC INPUTS (The kwargs part) ---
        # We ask for "extra" details without hardcoding variables
        while True:
            extra = input("Add more info? (type 'email', 'city', 'job' or 'no'): ").lower()
            if extra == "no":
                break
            # Use the input string as the Key!
            value = input(f"Enter {extra}: ")
            current_details[extra] = value 
        # --- THE MAGIC STEP ---
        # We pass 'current_details' using ** to unpack it into kwargs
        save_contact(data, name, **current_details)

# 7. Word Statistics Tool (Lambda + Functions)
# Problem:
# Analyze a sentence.
# Input:
# Sentence string
# Expected Behavior:
# Count total words
# Use lambda to count word lengths
# Print longest and shortest word
def sen_analyze():
    sent = input("Enter something: ")
    words = sent.split()
    if len(words) == 0:
        print("You didn't enter any words.")
        return
    # Define Lambda ONCE (Cleaner)
    # This acts just like len(), but it's your custom tool
    get_length = lambda x: len(x)
    longest = words[0]
    shortest = words[0]
    for word in words:
        # USE the lambda to compare lengths
        if get_length(word) > get_length(longest):
            longest = word
        # USE the lambda for shortest too
        if get_length(word) < get_length(shortest):
            shortest = word
    print(f"\nTotal words: {len(words)}")
    print(f"Longest word: '{longest}' ({get_length(longest)} chars)")
    print(f"Shortest word: '{shortest}' ({get_length(shortest)} chars)")
sen_analyze()

# 8. File-based Notes App
# Problem:
# Create a notes application.
# Input:
# Add note
# View notes
# Exit
# Expected Behavior:
# Notes stored in a text file
# Use functions for each operation
# Handle file not found error
# data = {"name": "Om Raj"}
# def notes_app():
#     print(f"Welcome {data['name']}")
#     while True:
#         action = input("\n1) Add Notes\n2) View Notes\n3) Exit\nChoose (1/2/3): ").strip()
#         try:
#             # --- EXIT ---
#             if action == "3":
#                 print("Exiting... Goodbye!")
#                 return
#             # --- ADD NOTES ---
#             if action == "1":
#                 topic = input("Enter Heading: ")
#                 brief = input("Enter the content: ")
#                 file_name = input("Enter the filename (e.g., notes.txt): ")
#                 # FIX 1: Use input(), not print()
#                 mode_choice = input("Want to append or write new? (a/w): ").lower().strip()
#                 # FIX 3: Actually set the mode variable based on user choice
#                 if mode_choice == "w":
#                     file_mode = "w"  # Overwrite
#                 else:
#                     file_mode = "a"  # Default to Append
#                 # Write to file
#                 with open(file_name, file_mode) as f:
#                     f.write(f"\n{topic}:\n\t{brief}\n")
#                 print(f"✅ Saved to {file_name} in '{file_mode}' mode.")
#             # --- VIEW NOTES ---
#             elif action == "2":
#                 # FIX 4: Ask which file to view
#                 read_file = input("Enter filename to read: ")
#                 try:
#                     with open(read_file, "r") as f:
#                         # FIX 2: Use parentheses ()
#                         content = f.read() 
#                         print("\n--- Note Content ---")
#                         print(content)
#                         print("--------------------")
#                 except FileNotFoundError:
#                     print(f"❌ Error: The file '{read_file}' does not exist.")
#         except Exception as e:
#             print(f"⚠️ An unexpected error occurred: {e}")
# notes_app()

data = {"name": "Om Raj"}
# --- Function 1: Add Note ---
def add_note():
    topic = input("Enter Heading: ")
    brief = input("Enter the content: ")
    file_name = input("Enter the filename (e.g., notes.txt): ")
    # Check mode (Append vs Write)
    mode = input("Want to append or write new? (a/w): ").lower().strip()
    if mode == "w":
        file_mode = "w"  # Wipes file clean
    else:
        file_mode = "a"  # Adds to end (Safer default)
    try:
        # FIX: Ensure we actually use the mode selected
        with open(file_name, file_mode) as f:
            f.write(f"\n{topic}:\n\t{brief}\n")
        print(f"✅ Saved to '{file_name}' in '{file_mode}' mode.")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
# --- Function 2: View Note ---
def view_note():
    # FIX: Ask which file to view (don't assume 'sample.txt')
    target_file = input("Enter filename to view: ")
    try:
        with open(target_file, "r") as f:
            # FIX: Added () to .read()
            content = f.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------")
    except FileNotFoundError:
        print(f"❌ Error: The file '{target_file}' was not found.")
# --- Main Controller ---
def notes_app():
    print(f"Welcome {data['name']}")
    while True:
        print("\n1) Add Notes")
        print("2) View Notes")
        print("3) Exit")
        action = input("Choose (1/2/3): ").strip()
        if action == "1":
            add_note()
        elif action == "2":
            view_note()
        elif action == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.")
# Run the app
notes_app()

# 9. Expense Tracker (Dictionary + Functions)
# Problem:
# Track daily expenses.
# Input:
# Category
# Amount
# Expected Behavior:
# Store expenses in dictionary
# Function to calculate total
# Function to display category-wise spending
# print("--- Track Daily Expense ---")
# data = {}
# def tracker():
#     category = input("Enter category (e.g., Food): ")
#     sub_cat = input("Enter product: ")
#     amount = float(input("Enter the amount: "))
#     # FIX 1: Check if the category acts as a KEY (Variable, no quotes)
#     if category not in data:
#         data[category] = [] # Create a new list for this category
#     # FIX 2: Create the entry and APPEND it to the list
#     entry = {
#         "sub_cat": sub_cat,
#         "amount": amount
#     }
#     data[category].append(entry)
#     print(f"✅ Saved {sub_cat} to {category}")
# def tot():
#     total = 0
#     # FIX 3: Loop through Categories, then Items
#     for cat, items_list in data.items():
#         for item in items_list:
#             total += item['amount']
#     print(f"💰 Total Bill: {total}")
# def show_item():
#     print("\n--- Summary ---")
#     for k, v in data.items():
#         # 'v' is now a list of items
#         print(f"- {k.upper()}: {v}")
# # --- Test Area ---
# while True:
#     choice = input("\n1) Add  2) Total  3) Show  4) Exit: ")
#     if choice == "1": tracker()
#     elif choice == "2": tot()
#     elif choice == "3": show_item()
#     elif choice == "4": break
# The Goal Structure
data = {
    "Food": [ 
        {"item": "Milk", "amount": 50}, 
        {"item": "Bread", "amount": 40} 
    ],
    "Travel": [
        {"item": "Bus", "amount": 20}
    ]
}
print("--- Daily Expense Tracker ---")
data = {}
def add_expense():
    category = input("Enter category (e.g., Food, Travel): ").capitalize()
    item_name = input("Enter item name: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return
    # 1. Check if category exists. If not, create an empty list.
    if category not in data:
        data[category] = []
    # 2. Append the new expense to that list
    # We store it as a small dictionary so we know what the money was for
    expense_entry = {"item": item_name, "amount": amount}
    data[category].append(expense_entry)
    print(f"✅ Added {amount} to {category}.")
def calculate_total():
    total_bill = 0
    # Loop through every category (Food, Travel...)
    for category_list in data.values():
        # Loop through every item in that category
        for entry in category_list:
            total_bill += entry['amount']
    print(f"\n💰 Total Bill: ₹{total_bill}")
def show_summary():
    print("\n--- Spending Summary ---")
    if not data:
        print("No expenses recorded yet.")
    for category, expense_list in data.items():
        # Calculate sub-total for this specific category
        cat_total = sum(item['amount'] for item in expense_list)
        print(f"📂 {category}: ₹{cat_total}")
        # Optional: Show details
        for entry in expense_list:
            print(f"   - {entry['item']}: ₹{entry['amount']}")
# --- Main Loop ---
while True:
    choice = input("\n1) Add  2) Summary  3) Total  4) Exit: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Exiting...")
        break

# 10. Custom Math Module
# Problem:
# Create your own math utility module.
# Input:
# Numbers for add, subtract, multiply
# Expected Behavior:
# Write functions in a separate .py file
# Import module in main program
# Use __name__ == "__main__"

# File Name: my_math.py
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
# --- THE GUARD BLOCK ---
# This code runs ONLY if you run 'my_math.py' directly.
# It will NOT run if you import this file into 'main.py'.
if __name__ == "__main__":
    print("--- Running Test (Developer Mode) ---")
    print(f"Test Add (5+5): {add(5, 5)}")
    print(f"Test Sub (10-2): {subtract(10, 2)}")
# File Name: main.py
import my_math  # This looks for 'my_math.py' in the same folder
print("--- Main App Started ---")
# Usage Style 1: Module.Function
res1 = my_math.add(10, 20)
print(f"Addition Result: {res1}")
# Usage Style 2: Import specific function
from my_math import multiply
res2 = multiply(5, 5)
print(f"Multiplication Result: {res2}")
