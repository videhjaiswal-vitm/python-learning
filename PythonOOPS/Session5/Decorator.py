'''
Decorator: 
It is a function that accept function as a argument and called inside wrapper function and return a function.
It takes result of function and modifies the result and return it.
Syntax:
use @decorator_name to specify a decorator to be applied on another function.
'''
def decorator1(f11):
    #wrapper
    def inner():
        f11() #calling f1 func
        print("World")
    return inner
@decorator1
def f1():
    print("Hello",end=" ") 
f1()
