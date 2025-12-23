# Project Requirements
# You will build a system that:
# Accepts multiple sentences
# Cleans the text
# Converts each sentence into list of words
# Removes duplicates using sets
# Stores everything in a dictionary
# Displays a summary

# MY APPROACH
#print("Hello! Welcome buddy")
# sentence_contain = []
# list_sent_contain = []
# while True:
#  a = print("Enter something or type 'quit' for exit: ")
#  if a.strip().lower() == 'quit':
#    break
# if a.stript().lower() != 'quit':
#    sentence_contain.append(a)
# for i in sentence_contain:
#  list_sent_contain.append(i)
# print(list_sent_contain)

# --- 1. Setup ---
# A dictionary to hold our "Database"
database = {
    "sentences": [],
    "unique_words": set()
}
print("Hello! Welcome buddy")
# --- 2. Input & Processing ---
while True:
    a = input("Enter sentence (or 'quit'): ")
    if a.strip().lower() == 'quit':
        break
    # PROCESS 1: Store Original
    database["sentences"].append(a)
    # PROCESS 2: Clean (Manual version)
    # Remove dots and make lowercase
    clean_a = a.replace(".", "").replace(",", "").lower()
    # PROCESS 3: Split into words
    # "Hello World" -> ["hello", "world"]
    words = clean_a.split() 
    # PROCESS 4: Add to Set (The Magic Step)
    database["unique_words"].update(words)
# --- 3. Output ---
print("\n--- SUMMARY ---")
print("Sentences stored:", database["sentences"])
print("Unique Vocabulary:", database["unique_words"])
