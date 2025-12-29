# 16. File Analyzer Tool
# Problem:
# Analyze text file content.
# Input:
# File name
# Expected Behavior:
# Count lines
# Count words
# Count characters
# Use error handling
def check_file():
    filename = input("Enter the filename: ")
    # Safety Check: valid extension?
    if not filename.endswith(".txt"):
        print("⚠️ Please enter a .txt file.")
        return
    try:
        with open(filename, "r") as f:
            # 1. Read the raw content ONCE
            content = f.read()
            # 2. Count Characters
            # (Use len() directly on the string)
            char_count = len(content)
            # 3. Count Words
            # (Split into a list of words, then count the list items)
            words_list = content.split()
            word_count = len(words_list)
            # 4. Count Lines
            # (Split by "newline" character, then count)
            # We use splitlines() which is safer than split("\n")
            lines_list = content.splitlines()
            line_count = len(lines_list)
            # --- DISPLAY RESULTS ---
            print("\n" + "="*20)
            print(f"📄 Analysis for: {filename}")
            print("-" * 20)
            print(f"📝 Lines:      {line_count}")
            print(f"🗣️  Words:      {word_count}")
            print(f"🔤 Characters: {char_count}")
            print("="*20)
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found!")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
check_file()

# 20. Mini CLI Utility App (Interview-Level)
# Problem:
# Build a command-based utility.
# Input Options:
# Calculator
# Notes
# File reader
# Exit
# Expected Behavior:
# Menu-driven system
# Each feature in separate function
# Proper exception handling
# import os
# import datetime
# --- FEATURE 1: CALCULATOR ---
# def calculator():
#     print("\n🧮 --- Calculator ---")
#     try:
#         num1 = float(input("Enter first number: "))
#         op = input("Enter operator (+, -, *, /): ").strip()
#         num2 = float(input("Enter second number: "))
#         if op == "+":
#             print(f"✅ Result: {num1 + num2}")
#         elif op == "-":
#             print(f"✅ Result: {num1 - num2}")
#         elif op == "*":
#             print(f"✅ Result: {num1 * num2}")
#         elif op == "/":
#             if num2 == 0:
#                 print("❌ Error: Cannot divide by Zero!")
#             else:
#                 print(f"✅ Result: {num1 / num2:.2f}") # .2f rounds to 2 decimals
#         else:
#             print("❌ Invalid Operator")
#     except ValueError:
#         print("❌ Error: Please enter valid numbers.")
# # --- FEATURE 2: NOTES MANAGER ---
# def notes_manager():
#     print("\n📝 --- Quick Notes ---")
#     note_text = input("Write your note: ")
#     # Get current time for the log
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#     entry = f"[{timestamp}] {note_text}\n"
#     try:
#         with open("utility_notes.txt", "a") as f:
#             f.write(entry)
#         print("✅ Note saved to 'utility_notes.txt'")
#     except Exception as e:
#         print(f"❌ Error saving note: {e}")
# # --- FEATURE 3: FILE READER ---
# def file_reader():
#     print("\n📂 --- File Reader ---")
#     filename = input("Enter filename to read (e.g., sample.txt): ")
#     if not os.path.exists(filename):
#         print(f"❌ Error: The file '{filename}' does not exist.")
#         return
#     try:
#         with open(filename, "r") as f:
#             print("\n--- File Content ---")
#             print(f.read())
#             print("--------------------")
#     except Exception as e:
#         print(f"❌ Error reading file: {e}")
# # --- MAIN CONTROLLER ---
# def main_menu():
#     print("\n" + "="*30)
#     print(" 🛠️  OM'S CLI UTILITY TOOL  🛠️")
#     print("="*30)
#     while True:
#         print("\nMAIN MENU:")
#         print("1) 🧮 Calculator")
#         print("2) 📝 Add Note")
#         print("3) 📂 Read File")
#         print("4) 🚪 Exit")
#         choice = input("Select Option (1-4): ").strip()
#         if choice == "1":
#             calculator()
#         elif choice == "2":
#             notes_manager()
#         elif choice == "3":
#             file_reader()
#         elif choice == "4":
#             print("👋 Goodbye! Closing Utility...")
#             break
#         else:
#             print("⚠️ Invalid choice. Try again.")
# # --- ENTRY POINT ---
# # This ensures the code runs only if executed directly
# if __name__ == "__main__":
#     main_menu()

# --- SIMPLIFIED CLI APP (No os/datetime) ---
def calculator():
    print("\n🧮 Calculator")
    try:
        n1 = float(input("Num 1: "))
        op = input("Op (+ - * /): ")
        n2 = float(input("Num 2: "))
        
        if op == "+": print(n1 + n2)
        elif op == "-": print(n1 - n2)
        elif op == "*": print(n1 * n2)
        elif op == "/": print(n1 / n2)
        else: print("Invalid Operator")
    except:
        print("Invalid Input")
def notes():
    print("\n📝 Notes")
    text = input("Write note: ")
    # Just save raw text
    with open("notes.txt", "a") as f:
        f.write(text + "\n") 
    print("Saved.")
def file_reader():
    print("\n📂 Reader")
    fname = input("Filename: ")
    try:
        # We try to open it directly. If it fails, the 'except' catches it.
        with open(fname, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("❌ File doesn't exist.")
# --- MAIN LOOP ---
while True:
    choice = input("\n1) Calc  2) Note  3) Read  4) Exit: ")
    if choice == "1": calculator()
    elif choice == "2": notes()
    elif choice == "3": file_reader()


# 21. Data Cleaner Tool
# Problem:
# Clean raw user input data.
# Input:
# List of mixed strings
# Expected Behavior:
# Remove spaces
# Convert to lowercase
# Remove duplicates using set
# Return clean list

# def cln():
#     with open(".txt","r") as f:
#         content = f.read()
#         lower_cont = content.lower()
#         rmv_spc = content.split()
#         set_cont = set(content)
#     print(rmv_spc)
#     print(lower_cont)
#     print(set_cont)
# cln()
def file_cleaner():
    filename = "sample.txt" # Make sure this file exists!
    try:
        with open(filename, "r") as f:
            content = f.read()
            # PIPELINE:
            # 1. Split into words (removes spaces/newlines automatically)
            words = content.split() 
            # 2. Convert all to lowercase
            # (We use a loop because .lower() only works on strings, not lists)
            lower_words = [w.lower() for w in words]
            # 3. Remove duplicates
            unique_words = set(lower_words)
            print(f"Original Words: {len(words)}")
            print(f"Unique Words:   {len(unique_words)}")
            print(unique_words)
    except FileNotFoundError:
        print("❌ File not found.")
file_cleaner()
