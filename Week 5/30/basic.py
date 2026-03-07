# 📅 DAY 30 — String Algorithms & Text Processing
# 🎯 Day-30 Objective
# By the end of today you will be able to:
# Analyze text using algorithms
# Clean and process sentences
# Count words and characters
# Build a word frequency analyzer
# Understand the foundation of NLP preprocessing
# This is extremely important because ML models often start with text cleaning.


# 🧠 PART 1 — Thinking Algorithmically About Text
# Example sentence:
# "Machine learning is powerful and learning is fun"
# Questions we may want to answer:
# How many words?
# Which word appears most frequently?
# How many unique words?
# How many characters?
# These are algorithmic text problems.


# 🧩 PART 2 — Basic String Algorithm Patterns
# 1️⃣ Counting Characters
text = "python"
count = 0
for ch in text:
    count += 1
print("Length:", count)
# 2️⃣ Counting Words
sentence = "machine learning is powerful"
words = sentence.split()
print("Word count:", len(words))
print(words)
# 3️⃣ Filtering Words
# Example: words longer than 5 characters
long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)
        

# 🧠 PART 3 — Word Frequency Algorithm
# Goal:
# Input:
# "python is great and python is powerful"
# Output:
# python : 2
# is : 2
# great : 1
# and : 1
# powerful : 1
# Algorithm:
# 1️⃣ Split sentence into words
# 2️⃣ Create dictionary
# 3️⃣ Loop through words
# 4️⃣ Update counts
# word = "python is great and python is powerful"
# words = word.split()
# empt_dict = {}
# count = 0
# for i in words:
#     if i not in empt_dict:
#         empt_dict[i] = count
#         count += 1
# print(f'{empt_dict}\n')
word = "python is great and python is powerful"
words = word.split()
empt_dict = {}
for i in words:
    if i not in empt_dict:
        empt_dict[i] = 1
    else:
        empt_dict[i] += 1
for key, value in empt_dict.items():
    print(f"{key} : {value}")
