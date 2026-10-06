import re

text = "My marks are 85, 90 and 75"

result = re.findall(r'\d+', text)

print(result)