file = open("student.txt", "r")

lines = file.readlines()

lines.reverse()

for line in lines:
    print(line, end="")

file.close()