s = input("Enter a string:")
result = ""
for i in s:
    if s.count(i) > 1 and i not in result:
        result += i

print("Duplicate charcter:",result)