# 📅 DAY 14 — FILE HANDLING
# 🎯 Day-14 Objective
# By the end of today, you will:
# Open, read, write, append files
# Work with .txt and .json
# Save processed data
# Load data back from the file
# Build an Exported Data Pipeline mini-project
# Push everything to GitHub
# This is exactly how ML pipelines work:
# Read → Clean → Process → Save → Load → Train Model

# 🧠 PART 1: Opening a File
file = open("demo.txt", "w")
file.write("Hello ML Engineer!")
file.close()
# | Mode   | Meaning           |
# | ------ | ----------------- |
# | `"w"`  | write (overwrite) |
# | `"a"`  | append            |
# | `"r"`  | read              |
# | `"w+"` | write + read      |

# 📝 PART 2: Writing to a File
with open("note.txt", "w") as f:
    f.write("This is a test file.\n")
    f.write("File handling is important.")

# 👀 PART 3: Reading from File
with open("note.txt", "r") as f:
    content = f.read()
    print(content)
# Read line by line
with open("note.txt", "r") as f:
    for line in f:
        print(line)

# 📌 PART 4: Appending to File
with open("note.txt", "a") as f:
    f.write("\nNew line added!")



# 🔁 PART 5: JSON Files (VERY IMPORTANT for ML)
# Because ML configs, datasets, metadata = JSON.
import json
data = {"name": "Raj", "age": 18}
with open("data.json", "w") as f:
    json.dump(data, f)
# Read JSON
with open("data.json", "r") as f:
    d = json.load(f)
    print(d)
