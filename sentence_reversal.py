s = input("Enter a sentence: ")
words = s.split()
reverse =""
for i in words:
    reverse = i + " " + reverse
print("Reversed sentence:", reverse)