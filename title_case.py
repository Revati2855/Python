s = input("Enter a string:")
word = s.split()
result=""
for i in word:
    result += i[0].upper() + i[1:] + " "
print("Title case: ",result)