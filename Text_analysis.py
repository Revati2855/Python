text = input("Enter a paragraph:\n")

words = text.lower().split()

print("\nTotal Number of Words:", len(words))

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 Most Frequent Words:")
for word, count in sorted_words[:3]:
    print(word, ":", count)

vowels = "aeiou"
vowel_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1

print("\nTotal Number of Vowels:", vowel_count)