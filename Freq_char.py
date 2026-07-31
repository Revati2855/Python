s = input("Enter a string:")
char = input("Enter a character to count:")
count = 0
for i in s:
    if i == char:
        count += 1
print("Fequency of", char, "is:", count)