'''
Encapsulation:It is a object Oriented Feature which signifys wrapping up of data into a single unit. It is used for security purpose.
'''
class Employee:

    def setDetails(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def getDetails(self):
        print("Employee ID:",self.eid)
        print("Employee Name:",self.ename) 
        print("================")

e=Employee()
print("=====Before Changes====")
e.setDetails(101,"Rahul Sharma")
e.getDetails()
e.eid=102
print("=====After Changes====")
e.getDetails()
