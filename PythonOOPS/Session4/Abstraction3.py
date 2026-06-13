
from abc import ABC,abstractmethod

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

    shapename="Square"
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

s1 = Square()
s1.side=23
s1.calArea()
s1.calPerimeter()
s1.display()
print("======================")

def fencingCharges(shape):
    print("Shape Name is:",shape.shapename)
    print("Charges is:",shape.perimeter*12)

print("================")

fencingCharges(r1)
fencingCharges(s1)

'''
Create abstract class Taxable with variables taxRate{get}, 
and function getTax()->Float
-
create class
Employee(id,name,salary) add display
function. 
Inherit Taxable abstract class.
Decide income taxRate 30% for salary
above 10 lac, 20% for salary between 5
and 10 lac and 6% for salary below 5 lac
-
create class Restaurent (restaurent
name, Bill amount). add display and
input function. decide GST 10% and
Inherit Taxable abstract class to getTax()

-
create 2 object of Employee and 3
Obj of RestaurentBill and print total
amount of tax on all 5 objects
-
Create Global function that accept
reference of type Taxable and print 5%
of refund on tax applied.
'''

