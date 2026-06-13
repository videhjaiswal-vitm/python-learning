
from abc import ABC,abstractmethod

#abstract class
class TwoDShape(ABC):

    area=0
    perimeter=0
    shapename=""

    @abstractmethod
    def calArea(self):
        pass

    @abstractmethod
    def calPerimeter(self):
        pass

#=========
class Rectangle(TwoDShape):

    shapename="Rectangle"
    length=0
    breadth=0

    def calArea(self):
        self.area=self.length*self.breadth

    def calPerimeter(self):
        self.perimeter=2*(self.length+self.breadth)

    def display(self):
        print("Shape Name:",self.shapename)
        print("Length is:",self.length)
        print("Breadth is:",self.breadth)
        print("Area is:",self.area)
        print("Perimeter is:",self.perimeter)

r1 = Rectangle()
r1.length=10
r1.breadth=23
r1.calArea()
r1.calPerimeter()
r1.display()

print("==============================")

class Square(TwoDShape):

    shapename="square"
    side=0

    def calArea(self):
        self.area=self.side*self.side

    def calPerimeter(self):
        self.perimeter=4*self.side

    def display(self):
        print("Shape Name:",self.shapename)
        print("Side is:",self.side)
        print("Area is:",self.area)
        print("Perimeter is:",self.perimeter)

r1 = Square()
r1.side=23
r1.calArea()
r1.calPerimeter()
r1.display()

'''
1. Create class Student with variable 
(name,course,dateOfBirth)- create SchoolStudent class with 
variable (fees) and inherit class Student
- create CollegeStudent with 
variable(sem and fees) and inherit class Student
- create class PGStudent with 
variable(mainSubject, percent) and 
inherit CollegeStudent
-add parameterized 
initializer in all classes

2. Create class Employee(id,name,salary) 
and add display function
- create class PartTimeEmployee with 
variable(hoursWorked , hourlyRate) and 
inherit - class Employee. 
Add calculateSalary() function to calcualte 
salary as
salary = hourlyRate * hoursWorked- create class FullTimeEmployee with 
variables(basic,da,pf) and Add 
calculateSalary() function to calcualte 
salary as
salary = basic + da - pf- add default and parameterized 
initializer in all classes
- Create a global function getTax() 
which accept Employee object in argument 
and calculate and print income tax on 
employee salary(12.5% of salary)
- Also try to pass Objects of 
PartTimeEmployee and FullTimeEmployee to 
getTax() method
'''