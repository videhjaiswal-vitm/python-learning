'''
Decorator: 
It is a function that accept a function as a argument and called inside wrapper function and return a function.
It takes result of function and modifies the result and return it.
Syntax:
use @decorator_name to specify a decorator to be applied on another function.
'''
def decorator1(func):
    def inner():
        result = func()+30 #20+30=50
        print("Result1 is:",result)
        return result
    return inner
def decorator2(func):
    def inner():
        result = func()+50 #50+50=100
        print("Result2 is:",result)
        return result
    return inner 
def decorator3(func):
    def inner():
        result = func()+100 #100+100=200
        print("Result3 is:",result)
    return inner 
@decorator3
@decorator2
@decorator1
def f1():
    return 20
f1()