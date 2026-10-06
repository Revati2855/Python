import re

pattern = re.compile(r'[0-9]+')

text = "Gouri123"

result = pattern.findall(text)

print(result)