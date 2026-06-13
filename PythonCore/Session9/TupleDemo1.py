'''
Tuple:It is a sequence which is used to store hetergenous data where each data is given by integer value.
Note:It is immutable(unchangable).
Syntax:
tupname=(e1,e2,.....en)
----------------------------
'''

emp_details=("Rahul Sharma",121,34567.34,"iOS Developer","rahul@gmail.com")
print(emp_details)
print("DataType is:",type(emp_details))
print("=================")

#acccess single data
print("emp_details[2]:",emp_details[2])
print("emp_details[-2]:",emp_details[-2])
print("=================")

#access all data with index
for index in range(len(emp_details)):
    print("Index:",index,"emp_details:",emp_details[index])
print("=================")

#access all data with index
for index in range(-len(emp_details),0):
    print("Index:",index,"emp_details:",emp_details[index])
print("=================")

#access all data without index
for data in emp_details:
    print("emp_details:",data)
print("=================")

