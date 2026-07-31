s = input("Enter a string:")
old = input("Enter character to replace:")
new = input("Enter new charcter:")
result = ""
for i in s:
    if i == old:
        result += new
    else:
        result += i
print("The new string is:", result)
