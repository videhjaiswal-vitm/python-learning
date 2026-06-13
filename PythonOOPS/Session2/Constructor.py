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
'''

class Student:

    #default constructor
    def __init__(self):
        print("call to init")
        self.college="Vikrant Group of institution"
        self.name="NA"
        self.rollno=0
        self.course="NA"
        self.fees=0.0

    def display(self):
        print("Name is:",self.name)
        print("Rollno is:",self.rollno)
        print("Course is:",self.course)
        print("Fees is:",self.fees)
        print("College:",self.college)
        print("========================")

s=Student()        
s.name="Priya Sharma"
s.rollno=101
s.course="B.Tech"
s.fees=45678.45
s.display()

s1=Student()        
s1.name="Mohan Sharma"
s1.rollno=102
s1.course="M.Tech"
s1.fees=45678.45
s1.college="IIT Indore"
s1.display()




