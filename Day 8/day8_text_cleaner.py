text = input("Enter a sentence: ")

clean = text.strip().lower().replace(",", "").replace(".", "")

print("Cleaned text:", clean)
