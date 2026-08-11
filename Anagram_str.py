def normalize(text):
    result = ""
    for ch in text.lower():
        if ch.isalnum():      
            result += ch
    return result

def frequency(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = normalize(str1)
str2 = normalize(str2)

if frequency(str1) == frequency(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")