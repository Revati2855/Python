s = input("Enter a string:")
reverse = ""
for i in s:
    reverse = i + reverse
if s == reverse:
    print("String is palindrome")
else:
    print("String is not palindrome")