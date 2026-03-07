text = input("Enter a sentence: ")
# clean text
text = text.lower()
words = text.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("\nWord Frequency:")
for word, count in freq.items():
    print(word, ":", count)


# 🧠 THINK LIKE A DATA ENGINEER
# Ask yourself:
# How would I remove punctuation?
# How would I count only unique words?
# How would I find the most frequent word?
# These questions lead to NLP and ML feature engineering.
