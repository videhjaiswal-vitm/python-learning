'''
Desicion making Control Statement:
nested if else

Syntax:
if condition :
    if condition :
       statement
    else:
       statement
else:
   if condition :
       statement
    else:
       statement   
'''

# Find max out of three values
x=52
y=43
z=34

if x>y:
    if x>z:
       print("x is greatest:",x)
    else:
       print("z is greatest:",z)
else:       
    if y>z:
       print("y is greatest:",y)
    else:
       print("z is greatest:",z)

