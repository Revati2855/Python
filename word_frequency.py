paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:")

for word in frequency:
    print(word, ":", frequency[word])