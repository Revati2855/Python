text = "Python is a very easy and popular programming language."

stop_words = {"is", "a", "very", "and", "the", "in", "of", "to"}

words = text.split()

filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original:", words)
print("After stop word removal:", filtered_words)