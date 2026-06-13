'''
Multilevel inheritance:
class A => class B => class C => class D
'''
class OneBHK:

    def __init__(self,room,hall,kitchen):
        self.room=room
        self.hall=hall
        self.kitchen=kitchen

    def getArea(self):
        return self.room+self.hall+self.kitchen

    def display(self):
        print("Room is:",self.room)
        print("Kitchen is:",self.kitchen)
        print("Hall is:",self.hall) 

# o1=OneBHK(110,140,90)
# o1.display()
# print("Area of OneBHK is:",o1.getArea())           
        