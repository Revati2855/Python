class Student:

    def __init__(self):
        self.__name = "Revati"      
        self.__age = 20              

    def __display(self):             
        print("Name:", self.__name)
        print("Age:", self.__age)

    def show(self):
        self.__display()

s1 = Student()

s1.show()