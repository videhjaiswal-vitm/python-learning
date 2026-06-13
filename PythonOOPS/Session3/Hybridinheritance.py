'''
Hybrid Inheritance:Combination of any two inheritance.
Hierarchical Inheritance
Multiple Inheritance 

                class A     class B

                    class C

                class D     class E
==================================
'''

class A:

    def __init__(self):
        print("A's init")
    
    def display(self):
        print("A's display!!")

class B:

    def __init__(self):
        print("B's init")
    
    def display(self):
        print("B's display!!")        

class C(A,B):

    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("C's init")
    
    def display(self):
        super().display()
        B.display(self)
        print("C's display!!")
#===
class D(C):

    def __init__(self):
        super().__init__()
        print("D's init")
    
    def display(self):
        super().display()
        print("D's display!!")  

D().display()