#Encapsulation

class Student:
    def __init__(self, name, mark, age):
        self.name = name
        self._mark = mark
        self.__age = age

    def display(self):
        print(f"Student name is {self.name}, age is {self.__age}, mark is {self._mark}")

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getMark(self):
        return self._mark
    
    def setMark(self, mark):
        self._mark = mark



student = Student("Tom", 98, 17)
student.display()
print(student.getAge())
student.setAge(18)
print(student.getAge())




