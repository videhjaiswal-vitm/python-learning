'''
class A:
    data member
    member method
class B(A):
    data member
    member method
============
super: it is a keyword which is used to call parent method, constructor and variable.    
'''
from Person import Person

class Employee(Person):

    def __init__(self,id,salary,designation,name,age,address):
        super().__init__(name,age,address) #call person class parameterized constructor
        self.id=id
        self.salary=salary
        self.designation=designation

    def show(self):
        print("Id:",self.id)
        print("Salary:",self.salary)
        print("Designation:",self.designation)

e1=Employee(101,23000,"web Developer","Mohan Sharma",23,"Indore M.P")
e1.display()
e1.show()