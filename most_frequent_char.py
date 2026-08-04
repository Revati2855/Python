s = input("Enter a string: ")

max_count = 0
most_frequent = ""

for ch in s:
    count = s.count(ch)

    if count > max_count:
        max_count = count
        most_frequent = ch

print("Most frequent character:", most_frequent)
print("Frequency:", max_count)