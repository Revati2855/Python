s = input("Enter a string:")
vowels = 0
cons = 0
space = 0
special = 0
digits = 0
for i in s:
    if i in "aeiouAEIOU":
        vowels += 1
    elif i.isalpha():
        cons += 1
    elif i.isdigit():
        digits += 1
    elif i == " ":
        space += 1
    else:
        special += 1
print("Vowels: ", vowels)
print("Constant: ",cons)
print("Digits: ",digits)
print("Space: ",space)
print("Special: ",special)