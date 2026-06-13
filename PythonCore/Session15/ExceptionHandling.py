'''
Exception Handling: It is mechanism which is used to handle exception are as follows: 
1.try and except block 
2.try and multiple except block
3.try and finally block
4.try,except and finally block
==========
try:
    statement which generates exception
except ExceptionName:
    print(msg)
rest of the code will run        
'''
try:
    print("=============== Before Exception Occur =====================")
    a=12
    b=0
    print("Result is:",a/b)
    print("=============== After Exception Occur =====================")
except ZeroDivisionError:
    print("Value of b must be greater than zero")
print("=============== After Exception Occur ==================== ")


