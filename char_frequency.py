s = input("Enter a string:")
for i in s:
    if i not in s[:s.index(i)]:
        print(i, ":", s.count(i))