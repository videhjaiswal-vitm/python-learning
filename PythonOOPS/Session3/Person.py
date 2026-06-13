'''
Inheritance: Code reusability.
when a child class inherit properties and features of a parent class and a child class have it's own properties and features.
===========
Types of Inheritance:
1.Single Level Inheritance.
class A (Super,Parent,Base) => class B(Subclass,Child,Derived)
================ 
'''

class Person:

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print("Name is:",self.name)  
        print("Age is:",self.age)  
        print("Address is:",self.address)
            








