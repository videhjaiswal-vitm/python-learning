
from OneBHK import OneBHK
from TwoBHK import TwoBHK
from ThreeBHK import ThreeBHK

def paintingCharges(flat):
    area = flat.getArea()
    charges = area*12
    return charges 


o1=OneBHK(110,140,90)
o1.display()
print("Area of OneBHK is:",o1.getArea())     
print("PaintingCharges of OneBHK is:",paintingCharges(o1))
print("========================")

t1=TwoBHK(110,140,90,120)
t1.display()
print("Area of TwoBHK is:",t1.getArea())  
print("PaintingCharges of TwoBHK is:",paintingCharges(t1))
print("========================")

t1=ThreeBHK(110,140,90,120,105)
t1.display()
print("Area of ThreeBHK is:",t1.getArea())  
print("PaintingCharges of ThreeBHK is:",paintingCharges(t1))
print("========================")
