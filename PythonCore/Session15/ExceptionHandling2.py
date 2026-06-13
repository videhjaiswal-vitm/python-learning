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
except ExceptionName:
    print(msg)
except ExceptionName:
    print(msg)        
rest of the code will run        
'''
try:
    print("=============== Before Exception Occur =====================")
    a=12
    b=2
    print("Result is:",a/b)
    #===
    stud_marks = [34,45,56,67,89]
    print("stud_marks[2]:",stud_marks[2])
    print("stud_marks[-2]:",stud_marks[-2])
    #===
    stud_record = {"name":"Rahul Sharma","age":23,"address":"Ujjain M.P"}
    print("Name is:",stud_record["name"])
    print("Age is:",stud_record["age"])
    print("Address is:",stud_record["address"])
    #===
    # fo=open("demo.txt","r")
    # fo.read()
    import time1
    print("Module imported Successfully!!!")
except ZeroDivisionError:
    print("Value of b must be greater than zero")
except IndexError:
    print("Index value is out of range")
except KeyError:
    print("Address is not defined")
except FileNotFoundError:
    print("File not exists!")
except Exception as e :
    print("Exception Occured:",e)    
print("=============== After Exception Occur ==================== ")


