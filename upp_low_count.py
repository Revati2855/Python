s = input("Enter a string:")
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("Upppercase :", upper)
print("Lowercase :", lower)