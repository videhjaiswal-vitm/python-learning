'''
Multilevel inheritance:
class A => class B => class C => class D
'''
from OneBHK import OneBHK
class TwoBHK(OneBHK):

    def __init__(self,room,hall,kitchen,secondroom):
        super().__init__(room,hall,kitchen) #call init of OneBHK
        self.secondroom=secondroom

    #method overriding:same name and same arguments    
    def getArea(self):
        return self.secondroom+super().getArea()

    def display(self):
        super().display()
        print("SecondRoom is:",self.secondroom)
       
# t1=TwoBHK(110,140,90,120)
# t1.display()
# print("Area of TwoBHK is:",t1.getArea())           
        