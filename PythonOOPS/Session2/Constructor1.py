'''
Constructor:
1.It is used to initalize an object of a class.
2.It is a member of a class.
3.It called automatically when we create an object of a class.
Syntax:
def __init__(self):
    statements...
=================== 
Type of Constructor:
1.Default 
2.Parameterized   
==================
Polymorphism:Poly(Many) Morphism(Forms)
1.Compile Time:
1.Overloading:same name but different arguments.
ex:Method Overloading and Constructor Overloading.
Note:Overloading does not support in Python.
==============================================
2.RunTime:
1.Overriding:same name and same arguments.
ex:Method Overriding.
================================================
'''

class Student:

    #default constructor
    # def __init__(self):
    #     print("call to init")
    #     self.college="Vikrant Group of institution"
    #     self.name="NA"
    #     self.rollno=0
    #     self.course="NA"
    #     self.fees=0.0

    #parameterized constructor
    def __init__(self,name,rollno,course,fees,college):
        self.college=college
        self.name=name
        self.rollno=rollno
        self.course=course
        self.fees=fees
    def display(self):
        print("Name is:",self.name)
        print("Rollno is:",self.rollno)
        print("Course is:",self.course)
        print("Fees is:",self.fees)
        print("College:",self.college)
        print("========================")
s=Student("Priya Sharma",101,"B.Tech",45678.45,"IIT Indore")
s.display()



'''
1. Create class Farmer with varibales 
(name, crop, earning).
- Create parameterized 
initializer.
- Create display function
- Compare earnings of two Farmers 
and print name and crop of farmer who 
earns more.
=================================================
2. Create class Circle with variable radius.
- Create parameterized initializer.
- Create display function to display 
radius and area.
- Create function isBiggerThan( c: 
otherCircle) -> Bool- Create Two objects and call all the 
above functions
'''

