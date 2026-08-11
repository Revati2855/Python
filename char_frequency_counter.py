text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nCharacter Frequencies:")
for ch, count in sorted_frequency:
    print(repr(ch), ":", count)