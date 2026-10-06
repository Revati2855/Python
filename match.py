import re

text = "Python123"

result = re.match(r'Python', text)

if result:
    print("Match Found")
else:
    print("No Match")