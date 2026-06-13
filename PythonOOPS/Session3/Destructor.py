'''
Destructor:
1.It is used to de-initialize an object.
2.It is a member of a class.
3.It called automatically when all execution are finished.
-----
Syntax:
def __del__(self):
    statements...
======================    
'''
class Student:
    #parameterized constructor
    def __init__(self,name,rollno,course,fees,college):
        self.college=college
        self.name=name
        self.rollno=rollno
        self.course=course
        self.fees=fees

    #Destructor
    def __del__(self):
        print("call when all execution is finished!!!")

    def display(self):
        print("Name is:",self.name)
        print("Rollno is:",self.rollno)
        print("Course is:",self.course)
        print("Fees is:",self.fees)
        print("College:",self.college)
        print("========================")
s=Student("Priya Sharma",101,"B.Tech",45678.45,"IIT Indore")
s.display()
s1=Student("Beena Sharma",102,"B.Tech",55678.45,"Vikrant College")
s1.display()