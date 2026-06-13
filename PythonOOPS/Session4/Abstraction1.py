class TwoDShape:

    area=0
    perimeter=0
    shapename=""

    def calArea(self):
        pass

    def calPerimeter(self):
        pass

#=========
class Rectangle(TwoDShape):

    shapename="Rectangle"
    length=0
    breadth=0

    def calArea(self):
        self.area=self.length*self.breadth

    # def calPerimeter(self):
    #     self.perimeter=2*(self.length+self.breadth)

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
# r1.calPerimeter()
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
