import re

def extract_phone_numbers(text):

    pattern = r'(?:\(\d{3}\)\s*|\b\d{3}[-. ]?)\d{3}[-.]?\d{4}\b'

    phone_numbers = re.findall(pattern, text)

    return phone_numbers

text = input("Enter a block of text: ")

numbers = extract_phone_numbers(text)

print("\nPhone numbers found:")

if numbers:
    for number in numbers:
        print(number)
else:
    print("No valid phone numbers found.")