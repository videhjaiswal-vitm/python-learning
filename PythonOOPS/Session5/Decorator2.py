'''
Decorator: 
It is a function that accept function as a argument and called inside wrapper function and return a function.
It takes result of function and modifies the result and return it.
Syntax:
use @decorator_name to specify a decorator to be applied on another function.
'''
def decorator1(func):
    def inner():
        print("=====Good Evening=====") 
        func()
    return inner 
def decorator2(func):
    def inner():
        print("=====Good Afternoon===") 
        func()
    return inner 
def decorator3(func):
    def inner():
        print("=====Good Morning=====") 
        func()
    return inner    
@decorator3
@decorator2
@decorator1
def f1():
    print("=====Good Night=======") 
f1()
