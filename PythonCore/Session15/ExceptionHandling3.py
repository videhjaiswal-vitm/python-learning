'''
Exception Handling: It is mechanism which is used to handle exception are as follows: 
1.try and except block 
2.try and multiple except block
3.try and finally block
4.try,except and finally block
==========
try:
    statement which generates exception
finally:
    print("Finally block is always executes!!!!")     
rest of the code will run        
'''
try:
    fo=open("demo.txt","r")
    fo.read()
    import time1
    print("Module imported Successfully!!!")
except FileNotFoundError:
    print("File not exists!")
except Exception as e :
    print("Exception Occured:",e)  
finally:
    print("Finally block is always executes!!!!")       
print("=============== After Exception Occur ==================== ")


