'''
Tuple:It is a sequence which is used to store hetergenous data where each data is given by integer index.
Note:It is immutable(unchangable).
Syntax:
tupname=(e1,e2,.....en)
----------------------------
stud_marks=(45)
print(stud_marks)
print("DataType is:",type(stud_marks)) #int
print("=================")
stud_marks=(45,)
print(stud_marks)
print("DataType is:",type(stud_marks))
print("=================")
'''

stud_marks=(45,56,67,78,89)
#+ve index   0  1  2  3  4
#-ve index  -5 -4 -3 -2 -1
print(stud_marks)
print("DataType is:",type(stud_marks))
print("=================")

#acccess single data
print("stud_marks[2]:",stud_marks[2])
print("stud_marks[-2]:",stud_marks[-2])
print("=================")

#access all data with index
for index in range(len(stud_marks)):
    print("Index:",index,"stud_marks:",stud_marks[index])
print("=================")

#access all data with index
for index in range(-len(stud_marks),0):
    print("Index:",index,"stud_marks:",stud_marks[index])
print("=================")

#access all data without index
for data in stud_marks:
    print("stud_marks:",data)
print("=================")

#nested tuple
stud_record = ("Neha Sharma",121,5,(45,56,67,78,89),"BCA")
print(stud_record)
print(stud_record[3])
print(stud_record[3][1])
print("=================")

#access all data
for m in stud_record[3]:
    print(m)
print("=================")

#convert tuple into list
employee = ("Mohan Sharma",121,20000.0,"IT")

l=list(employee)
print(l)
print(type(l))

l[2]=50000.0
print(l)

#convert list into tuple
employee=tuple(l)
print(employee)
print(type(employee))

#record
e1 = ("Priya Sharma",121,"Android Developer",23456.23)
e2 = ("Raj Verma",122,"React Native Developer",45456.23)
e3 = ("Muskan Sharma",123,"Python Django Developer",53456.23)
e4 = ("Mohan Sharma",124,"Web Developer",28456.23)
e5 = ("Rakesh Sharma",125,"ASP.NET Developer",23456.23)

#add above data into a list
#list of tuple
emplist = []
emplist.append(e1)
emplist.append(e2)
emplist.append(e3)
emplist.append(e4)
emplist.append(e5)
print(emplist)

print("********** Employee Details ***************")
for index in range(len(emplist)):
    print(emplist[index][0],emplist[index][1],emplist[index][2],emplist[index][3])



































