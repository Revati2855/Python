s = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in s:
    if ch.isupper():
        encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch

print("Encrypted message:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isupper():
        decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
    elif ch.islower():
        decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch

print("Decrypted message:", decrypted)