s = input("Enter a sentence:")
word = input("Enter a word: ")
words = s.split()
count = 0
for i in words:
    if i == word:
        count += 1
print("Occurrences:", count)