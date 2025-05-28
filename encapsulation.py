#Encapsulation

class Student:
    """
    This is a base class for all students.

    Attributes:
            name (string): name of the student, initializes public attribute
            _mark (int): mark of the student, initializes protected attribute
            __age (int): age of the student, initializes private attribute 
    """

    def __init__(self, name, mark, age):
        """
        Initializes a Student instance.

        Args:
            name (string): name of the student, initializes public attribute
            mark (int): mark of the student, initializes protected attribute
            age (int): age of the student, initializes private attribute
        """
        self.name = name
        self._mark = mark
        self.__age = age

    def display(self):
        """
        Prints the student's attributes
        """
        print(f"Student name is {self.name}, age is {self.__age}, mark is {self._mark}")

    def getAge(self):
        """
        Gets the age of the student

        Returns:
            int: Student's current age
        """
        return self.__age
    

    def setAge(self, age):
        """
        Sets student's age.

        Args:
            age (int): The new age value
        """
        self.__age = age


    def getName(self):
        """
        Gets the name of the student

        Returns:
            string: Student's name
        """
        return self.name
    

    def setName(self, name):
        """
        Sets student's name.

        Args:
            name (string): Name of the student
        """
        self.name = name


    def getMark(self):
        """
        Gets the mark of the student

        Returns:
            int: Student's current mark
        """
        return self._mark
    

    def setMark(self, mark):
        """
        Sets student's mark.

        Args:
            mark (int): The new mark value
        """
        self._mark = mark



#create Student object with name, mark and age
student = Student("Tom", 98, 17)

#print attributes
student.display()

#get student's current age
print(student.getAge())

#set student's updated age 
student.setAge(18)

#get student's updated age 
print(student.getAge())




