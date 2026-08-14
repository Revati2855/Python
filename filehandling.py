file = open ("demo.txt","w")
file.write("Hello World\n")
file.write("This is file handling program.")
file.close()
print("File created successful.")

file = open("demo.txt","r")
print("\nUsing read():")
print(file.read())
file.close()

file = open("demo.txt","r")
print("\nUsing readline():")
print(file.readline())
file.close()

file = open("demo.txt","r")
print("\nUsing readlines():")
print(file.readlines())
file.close()

with open("demo.txt","r") as file:
    print("\nUsing with open.")
    print(file.read())

with open("demo.txt","w") as file:
    file.write("\nThis is write mode.")
print("Write operation completed.")

with open("demo.txt","a") as file:
    file.write("\nThis line is added using append.")
print("Appended successfully.")

with open("demo.txt","r+") as file:
    print("\nUsing r+:")
    print(file.read())
    file.write("\nThis is using r+")

with open("wplus.txt", "w+") as file:
    file.write("Hello from w+ mode.")
    file.seek(0)
    print("\nw+ mode:")
    print(file.read())

try:
    with open("newfile.txt", "x") as file:
        file.write("This file is created using x mode.")
    print("\nx mode: New file created successfully.")

except FileExistsError:
    print("\nx mode: File already exists.")


with open("demo.txt", "r") as file:
    file.seek(0)
    print("\nseek(0):")
    print(file.read())
    file.seek(6)
    print("\nseek(6):")
    print(file.read())


with open("demo.txt", "r") as file:
    print("\nInitial position:")
    print(file.tell())
    file.read(5)
    print("Position after reading 5 characters:")
    print(file.tell())



file.close()
print("File closed after close():", file.closed)
