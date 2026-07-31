s = input("Enter a string:")
words = s.split()
long = words[0]
for i in words:
    if len(i) > len(words):
        long = i

print("Longest word:", long)