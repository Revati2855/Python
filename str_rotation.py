s1 = input("Enter 1st string:")
s2 = input("Enter 2nd string:")
if len(s1) == len(s2) and s2 in s1 + s1:
    print("Yes, it is a rotation")
else:
    print("No, it is not a rotation")