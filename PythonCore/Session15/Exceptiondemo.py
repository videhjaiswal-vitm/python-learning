'''
Exception:It is a run time error when it occurs, program terminates.
Types of Exception:
1.NameError
2.ZeroDivisionError
3.IndexError
4.KeyError
5.TypeError
6.ValueError
7.FileNotFoundError
8.ModuleNotFoundError
============================================
print("=============== Before Exception Occur =====================")
name="Videh Jaiswal"
print("Name is:",name)
#NameError: name 'name' is not defined
print("=============== After Exception Occur =====================")
#=====
print("=============== Before Exception Occur =====================")
a=12
b=0
print("Result is:",a/b)
#ZeroDivisionError: division by zero
print("=============== After Exception Occur =====================")
#=========
print("=============== Before Exception Occur =====================")
stud_marks = [34,45,56,67,89]
print("stud_marks[22]:",stud_marks[22])
print("stud_marks[-22]:",stud_marks[-22])
#IndexError: list index out of range
print("=============== After Exception Occur =====================")
#========
print("=============== Before Exception Occur =====================")
stud_record = {"name":"Rahul Sharma","age":23}
print("Name is:",stud_record["name"])
print("Age is:",stud_record["age"])
print("Address is:",stud_record["address"])
#KeyError: 'address'
print("=============== After Exception Occur =====================")
#=========
print("=============== Before Exception Occur =====================")
fn="Videh"
ln="Jaiswal"
age=23
r=fn+ln+age
print(r)
#TypeError: can only concatenate str (not "int") to str
print("=============== After Exception Occur =====================")
#=========
print("=============== Before Exception Occur =====================")
def empdetails(name,age):
    print("name is:",name)
    print("age is:",age)
empdetails("Mohan Sharma")
#TypeError: empdetails() missing 1 required positional argument: 'age'
print("=============== After Exception Occur =====================")
#==========
print("=============== Before Exception Occur =====================")
gender="Male"
gender=int(gender)
print(gender)
#ValueError: invalid literal for int() with base 10: 'Male'
print("=============== After Exception Occur =====================")
#=======
print("=============== Before Exception Occur =====================")
fo=open("demo.txt","r")
fo.read()
#FileNotFoundError: [Errno 2] No such file or directory: 'demo.txt'
print("=============== After Exception Occur =====================")
'''

print("=============== Before Exception Occur =====================")
import time1
print("Module imported Successfully!!!")
#ModuleNotFoundError: No module named 'time1'
print("=============== After Exception Occur =====================")















