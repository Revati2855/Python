class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Destructor called")

s1 = Student("Riya", 20)

s1.display()