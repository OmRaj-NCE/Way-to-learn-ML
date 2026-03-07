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
