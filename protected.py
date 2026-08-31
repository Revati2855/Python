class Student:

    def __init__(self):
        self._name = "Revati"      
        self._age = 20             

    def _display(self):             
        print("Name:", self._name)
        print("Age:", self._age)

s1 = Student()

s1._display()

print(s1._name)
print(s1._age)