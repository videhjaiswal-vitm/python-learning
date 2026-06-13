'''
OOPS:Object Oriented Programming Structure.
Object:Any real World Entity.
ex:table,chair etc
=========
Properties:Shape,Size,Color,Weight,Height,Width,Price etc
========
Behaviour(Features):
Chair:
1.Sitting
2.Move
3.Rotate
==========
Bottle:
properties:
1.capacity in volumn
2.price
3.color
4.brand
5.material
==========================
class:
1.It is a blue print of an Object.
2.It is a collection of an Object.
3.It is a user defined datatype.
4.It is a collection of variables/attributes/properties and features/behaviour/methods.
-------
Difference between method and function:
-------
a function is a standalone block of code, 
while a method is a function that "belongs" to an object or class.
Feature: Definition                           
Function: Defined outside of any class. 
Method: Defined inside a class.
==============================
Feature: Association                           
Function: Independent; not tied to an object. 
Method: Associated with an object or class.
==============================
Feature:Calling
Function:Called by its name: my_func().
Method:Called on an object: my_obj.my_method()
==============================
Feature:Data Access
Function:Only accesses data passed to it.
Method:Can access/modify the object's internal data.
==============================
Object:Memory
1.It is an instance(example) of a Class.
===============================================
Syntax:
class: It is a keyword
class ClassName:
    "document.............."
    data member
    member methods
#==========       
self:It is a reference to a current class object.
'''
class Bottle:
    "This is a class to store bottle information"
    #instance variable or object variable
    # capacity_in_volumn
    # price
    # color
    # brand
    # material    

    def getBottleInfo(self):
        print(self)
        self.capacity_in_volumn=int(input("Enter a Bottle Capacity in Volumn\n"))
        self.price=float(input("Enter a Bottle Price\n"))
        self.color=input("Enter a Bottle Color\n")
        self.brand=input("Enter a Bottle Brand\n")
        self.material=input("Enter a Bottle material\n")

    def display(self):
        print("Capacity:",self.capacity_in_volumn)
        print("Price:",self.price)
        print("Color:",self.color)
        print("Brand:",self.brand)
        print("Material:",self.material)
        print("==================")

#create object
b=Bottle()
print("b:",b)
b.getBottleInfo() #pass internally reference to a method

b1=Bottle()
b1.getBottleInfo() #pass internally reference to a method
b1.display()
b.display()