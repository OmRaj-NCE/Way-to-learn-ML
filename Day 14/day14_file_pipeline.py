Project Requirement: 
Take multiple sentences
Clean them
Store in dictionary
Save dictionary to JSON file
Read JSON file back
Show loaded results

#import json
#data = {"name": "Raj", "age": 18}
#with open("data.json", "w") as f:
#    json.dump(data, f)

# 1. Setup a blank dictionary
import json
user_profile = {}
unique_words = set()
print("--- Dynamic Profile Builder ---")
while True:
    key = input("Enter Key (e.g., name, age) or 'quit': ").strip()
    if key.lower() == 'quit':
        break    
    value = input(f"Enter Value for '{key}': ")
    user_profile[key] = value
    clean_val = value.replace(".", "").lower()
    unique_words.update(clean_val.split())
print("\n--- FINAL DATABASE ---")
# This prints the dictionary nicely
for key, val in user_profile.items():
    print(f"{key}: {val}")
print("\nAll Unique Words Used:", unique_words)
with open("data.json", "w") as f:
    json.dump(user_profile, f)



import json
def clean(text):
    text = text.lower().strip()
    for ch in [".", ",", "!", "?", ":"]:
        text = text.replace(ch, "")
    return text
n = int(input("How many sentences? "))
sentences = []
cleaned_sentences = []
for i in range(n):
    s = input(f"Sentence {i+1}: ")
    sentences.append(s)
    cleaned_sentences.append(clean(s))
data = {
    "original": sentences,
    "cleaned": cleaned_sentences
}
# SAVE TO FILE
with open("cleaned_data.json", "w") as f:
    json.dump(data, f, indent=4)
print("\nData saved to cleaned_data.json")
# LOAD BACK FROM FILE
with open("cleaned_data.json", "r") as f:
    loaded = json.load(f)
print("\n--- LOADED DATA ---")
print(loaded)
