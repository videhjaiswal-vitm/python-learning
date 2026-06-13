'''
Access Specifier:To achieve Encapsulation we have to use access specifier to provide security.
=====
Public Member:Those members which are generated without any additional naming convention.
ex: data(),count
========
Private Member:Those members which are generated with __ start of name are private.
ex:__data(),__count
'''

class Employee:

    def __init__(self):
        print("call init")

    def setDetails(self,eid,ename):
        self.__eid=eid
        self.ename=ename
        
    def getDetails(self):
        print("Employee ID:",self.__eid)
        print("Employee Name:",self.ename) 
        print("================")


e=Employee()
print("=====Before Changes====")
e.setDetails(101,"Rahul Sharma")
e.getDetails()
e.__eid=102
print("=====After Changes====")
e.getDetails()

