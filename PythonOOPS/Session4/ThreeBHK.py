'''
Multilevel inheritance:
class A => class B => class C => class D
'''

from TwoBHK import TwoBHK

class ThreeBHK(TwoBHK):

    def __init__(self,room,hall,kitchen,secondroom,thirdroom):
        super().__init__(room,hall,kitchen,secondroom) #call init of TwoBHK
        self.thirdroom=thirdroom

    #method overriding:same name and same arguments    
    def getArea(self):
        return self.thirdroom+super().getArea()
        
    def display(self):
        super().display()
        print("ThirdRoom is:",self.thirdroom)
       
# t1=ThreeBHK(110,140,90,120,105)
# t1.display()
# print("Area of ThreeBHK is:",t1.getArea())           
        