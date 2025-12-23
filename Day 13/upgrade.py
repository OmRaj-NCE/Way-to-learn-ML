# 🧠 THINK LIKE AN ENGINEER
# Ask yourself:
# How would I add stopword removal?
# How would I count word frequencies?
# How would I store this in a JSON file?
# Can I extend this for a chatbot dataset?

# Define your "Stopwords"
# A manual list of common boring words
STOPWORDS = {"is", "the", "a", "an", "and", "of", "to", "in", "it", "this", "that"}
# --- 1. Setup ---
STOPWORDS = {"is", "the", "a", "an", "and", "of", "to", "in", "it", "this", "that"}
database = {
    "sentences": [],
    "unique_words": set() # Our Vocabulary
}
print("--- AI Text Preprocessor ---")
while True:
    a = input("Enter sentence (or 'quit'): ")
    if a.strip().lower() == 'quit':
        break       
    database["sentences"].append(a)
    clean_text = a.replace(".", "").replace(",", "").lower()
    all_words = clean_text.split()
    meaningful_words = []
    for word in all_words:
        if word not in STOPWORDS:
            meaningful_words.append(word)
    database["unique_words"].update(meaningful_words)
    print(f" -> Original: {all_words}")
    print(f" -> Meaningful: {meaningful_words}")
print("\n--- FINAL VOCABULARY ---")
print(database["unique_words"])


# Example - Sentences stored: ['hi. baby, my name is om, what about you.', 'quir', 'wecd']
# Unique Vocabulary: {'you', 'name', 'my', 'baby', 'hi', 'om', 'what', 'quir', 'is', 'about', 'wecd'}
# we can run a for loop and a = 0 b = [] to check if already exist in then pass otherwise fill.


import json # We import this to print the final data nicely
# 1. Initialize the main list
intents_list = []
print("--- Chatbot Dataset Builder ---")
while True:
    print("\n--- New Entry ---")
    # 1. Ask for the Category (Intent)
    tag = input("Intent (e.g., 'greeting', 'weather') or 'quit': ").lower().strip()
    if tag == 'quit':
        break
    # 2. Ask for the User's Message (Pattern)
    pattern = input(f"What does the user say for '{tag}'? : ")
    # 3. Ask for the Bot's Reply (Response)
    response = input(f"What should the bot reply? : ")
    # --- INTELLIGENT STORAGE ---
    # Check if this tag already exists in our list
    found = False
    for intent in intents_list:
        if intent["tag"] == tag:
            # If tag exists, just add the new pattern/response to it
            intent["patterns"].append(pattern)
            intent["responses"].append(response)
            found = True
            print(f"Updated existing tag: {tag}")
            break
    # If tag doesn't exist, create a new dictionary for it
    if not found:
        new_entry = {
            "tag": tag,
            "patterns": [pattern],
            "responses": [response]
        }
        intents_list.append(new_entry)
        print(f"Created new tag: {tag}")
# --- FINAL OUTPUT ---
# We wrap it in a final dictionary structure
final_dataset = {"intents": intents_list}
print("\n--- YOUR DATASET (JSON) ---")
# json.dumps prints it as a formatted string so you can copy-paste it
print(json.dumps(final_dataset, indent=4))
