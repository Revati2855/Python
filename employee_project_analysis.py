project1 = {"Aayush", "Mihir", "Isha", "Samu"}
project2 = {"Samu", "Riya", "Mihir", "Atharv"}

print("Employees in Project 1:", project1)
print("Employees in Project 2:", project2)

print("\nEmployees working on both projects:")
print(project1.intersection(project2))

print("\nEmployees only in Project 1:")
print(project1.difference(project2))

print("\nEmployees only in Project 2:")
print(project2.difference(project1))

print("\nTotal Unique Employees:")
print(project1.union(project2))