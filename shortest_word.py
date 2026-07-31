s = input("Enter a string:")
words = s.split()
short = words[0]
for i in words:
    if len(i) < len(words):
        short = i
print("Shortest word:", short)