s = input("Enter a string:")
result =""
for i in s:
    if i != " ":
        result += i
print("Without space:", result)