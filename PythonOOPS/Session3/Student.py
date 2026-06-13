'''
Hierarchical Inheritance: Tree Structure

                class A(Person)

    class B(Employee)      class C(Student)                
    
class D      class E    class F     class G         
===========================================         
'''

from Person import Person

class Student(Person):

    def __init__(self, name, age, address, rollno, course, fees):
        super().__init__(name, age, address)
        self.rollno=rollno
        self.course=course
        self.fees=fees
    #===
    def display(self):
        super().display()    
        print("Rollno is:",self.rollno)
        print("Course is:",self.course)
        print("Fees is:",self.fees)
    #==
#===
s=Student("Priya Verma",23,"Ujjain M.P",232,"M.Tech",56789.45)
s.display()

