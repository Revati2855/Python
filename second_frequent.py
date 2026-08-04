s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

values = sorted(set(frequency.values()), reverse=True)

if len(values) >= 2:
    second_max = values[1]

    for ch in s:
        if frequency[ch] == second_max:
            print("Second most frequent character:", ch)
            break
else:
    print("No second most frequent character")