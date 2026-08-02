s = input("Enter a password: ")
uppercase = False
lowercase = False
digits = False
special = False

for i in s:
    if i.isupper():
        uppercase = True
    elif i.islower():
        lowercase = True
    elif i.isdigit():
        digits= True
    else:
        special = True

if len(s) >= 8 and uppercase and lowercase and digits and special:
    print("Valid password.")
else:
    print("Invalid password.")