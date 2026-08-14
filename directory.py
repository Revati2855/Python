import os

print("Current Directory:")
print(os.getcwd())

os.mkdir("MyFolder")
print("Directory created successfully.")

os.rename("MyFolder", "NewFolder")
print("Directory renamed successfully.")

os.chdir("NewFolder")
print("Changed Directory:")
print(os.getcwd())

os.chdir("..")
print("Back to:")
print(os.getcwd())

print("Files and Folders:")
print(os.listdir())