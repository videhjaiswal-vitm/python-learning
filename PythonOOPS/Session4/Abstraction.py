'''
Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. This is one of the core concepts of object-oriented programming (OOP) languages.

Abstract Class:
It declares only function but do not have body in the function.
We can not create object of a abstract class.
'''

class Test:
    
    def demo(self):
        pass


class Demo(Test):

    def demo(self):
        print("Demo Class")

Demo().demo()
