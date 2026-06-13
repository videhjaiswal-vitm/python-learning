'''
input(): 
It is a predefined function to get data from a user.
It always return string
'''
name=input("Enter a name\n")
age=int(input("Enter a age\n"))
salary=float(input("Enter a salary\n"))

print("Name is:",name)
print("Data Type is:",type(name))
print("===============")
print("Age is:",age)
print("Data Type is:",type(age))
print("===============")
print("Salary is:",salary)
print("Data Type is:",type(salary))