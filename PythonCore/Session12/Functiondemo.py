'''
Function: It is a block of code which is used to perform a particular task.
It is used to reduce code.
Syntax:
def : keyword
def funcname(arguments):
    statements... 
    return value
==================
On the basis of Return Value and Arguments functions are classified into four category:
1.function without return type and without arguments.
2.function without return type and with arguments.
3.function with return type and without arguments.
4.function with return type and with arguments.
'''

#Type 1:
def greeting():
    print("Good Afternoon!!!")

greeting()

#Type 2:
def add(a,b):
    c=a+b 
    print("Addition is:",c)

add(23,34)

#Type 3:
def multiply():
    c=a*b 
    return c

a=12
b=12
r=multiply()
print("Multiplication is:",r)

#Type 4:
def cube(a):
    return a*a*a 

print("Cube is:",cube(12))  
print("===================================")

def empdetails(name,id):
    print("Name is:",name)
    print("Id is:",id)

#empdetails("Mohan Sharma",232)
#empdetails("Mohan Sharma")
#TypeError: empdetails() missing 1 required positional argument: 'id'

#keyword argument
def stud_details(name,rollno,course,fees):
    print("Name is:",name)
    print("Rollno is:",rollno)
    print("Course is:",course)
    print("Fees is:",fees)

#stud_details("Priya Sharma",121,"B.Tech",45678.45)
#stud_details(121,"Priya Sharma",45678.45,"B.Tech")
stud_details(rollno=121,name="Priya Sharma",fees=45678.45,course="B.Tech")
print("===================")

#default argument
#error:Non-default argument follows default argument
#def person_details(city="Indore",name,age,address):
def person_details(name,age,address,city="Indore"):
    print("Name is:",name)
    print("Age is:",age)
    print("Address is:",address)
    print("City is:",city)
    print("===================")


person_details("Raj Kumar",23,"56 Dhukan Indore M.P")
person_details("Raj Kumar",23,"Dewas Gate Ujjain M.P","Ujjain")
print("=============")

#recursion : function calling itself.
#5! = 5x4x3x2
def fact(n):
    total=0
    if n==1:
       return 1
    else:
       total=n*fact(n-1) # 5*4*3*2
       print(n,total)
       return total 
print("Factorial is:",fact(5))    
#====================================================

#immutable object:Tuple,integer,Float,String
def demo(a):
    print("a is:",a,"Memory Address is:",id(a))
    a+=25
    print("a is:",a,"Memory Address is:",id(a))
  
a=12
demo(a)
print("=================")

def getdata(l):
    print("l1 is:",l,"Memory Address1 is:",id(l))
    l.append(60)
    l.append(70)
    l.append(80)
    l.append(90)
    l.append(100)
    print("l2 is:",l,"Memory Address2 is:",id(l))


l=[10,20,30,40,50]
getdata(l)
print("l3 is:",l,"Memory Address3 is:",id(l))


def getdata1(l):
    print("l11 is:",l,"Memory Address11 is:",id(l))
    l=[11,22,33,44,55]
    print("l21 is:",l,"Memory Address21 is:",id(l))


l1=[10,20,30,40,50]
getdata1(l1)
print("l3 is:",l1,"Memory Address31 is:",id(l1))

print("===================")

'''
lambda function:
It is a anonymous(without name) function.
It can take any number of arguments, but can only have one expression.
It returns a function.
Their is no need to write return keyword.
================
Syntax:
lambda arguments : expression
'''
#no arguments
greeting = lambda : print("Good Evening!!!")
greeting()

#pass an argument
x = lambda a : a*a*a
print("Cube is:",x(10))

#pass multiple argument
x = lambda a,b : a+b
print("Addition is:",x(10,20))

#pass multiple argument
x = lambda a,b,c : a+b+c
print("Addition1 is:",x(10,20,30))

#pass multiple argument
t = lambda x,y : (x+y,x-y)
print("Tuple is:",t(12,23))

#if else
#lambda arguments : statements if condition else statements
result = lambda a,b : a+b if a>b else a*b 
print(result(3,4))




'''
Functions 
1. create a function to print greater of 
two numbers passed in argument
2. Create a function to print greater of 
three numbers passed in  argument
3. create a function to calculate and 
return factorial of a number passed in 
argument
4. create a function  which accepts an 
array of Int in argument and print sum 
of all elements
5. Create a function that accept two Int 
arrays and return sum of all elements of 
both arrays
6. Create a function that accepts two 
tuples of type (Float,Int) and return 
t1.0/t2.0 + t1.1*t2.1
'''

#1. create a function to print greater of 
#two numbers passed in argument
def test(a,b):
    if a>b:
       print("a is greatest:",a)
    else:    
       print("b is greatest:",b)

test(23,45)
print("===================")

#lambda arguments : statements if condition else statements
demo = lambda a,b : print("a is greatest:",a) if a>b else print("b is greatest:",b)
demo(23,34)

'''
3. create a function to calculate and 
return factorial of a number passed in 
argument
'''
def fact(n):
    f=1
    for a in range(1,n+1): 
        f=f*a 
    return f     

print("factorial is:",fact(4))

#squares = lambda n: [i**2 for i in range(1,n+1)]
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print("factorial is:",factorial(6))



































































