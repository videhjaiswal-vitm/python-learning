'''
Nested For Loop:
Syntax:
for varname in range(stop):  #row
    for varname in range(stop): #column
        statement...
    #===
    for varname in range(stop): #column
        statement...
    #===
#===
=============================
   c1c2c3c4c5
r1 * * * * *
r2 * * * * *
r3 * * * * *
r4 * * * * *

row col 
 0   0     
 0   1     
 0   2      
 0   3  
 0   4   
 -----
 1   0 
 1   1
 1   2
 1   3
 1   4  
 -----
 2   0
 2   1
 2   2
 2   3
 2   4   
 -----
 3   0
 3   1
 3   2
 3   3
 3   4        
'''

for row in range(4): # 0 1 2 3
    for col in range(5): # 0 1 2 3 4
        print("*",end=" ")
    print()    
print("===============")
'''
*
**
***
****
*****
------
row col
 0   0
'''
for row in range(5): # 0 1 2 3 4
                   #(1)
                   #(2)
                   #(3)
                   #(4)
                   #(5)
    for col in range(row+1):
        print("*",end="")
    print()
print("=================")

'''
============
$$$$*
$$$**
$$***
$****
*****
'''
for row in range(5,0,-1):
    #dollar          5-1=4
    #               (4) 0 1 2 3
    #               (3) 0 1 2
    #               (2) 0 1
    #               (1) 0  
    for col in range(row-1):
        print(" ",end="")
    #content        (5,6)
    #               (4,6) 
    for col in range(row,6):
        print("*",end="")    
    print()   
print("==============")     
'''
============
$$$$*
$$$***
$$*****
$*******
*********
'''
for row in range(5,0,-1):
   
    for col in range(row-1):
        print(" ",end="")
    
    for col in range(row,6):
        print("*",end="")    

    for col in range(row,5):
        print("*",end="")        
    print()  
print("==============")       
'''
============
$$$$*
$$$***
$$*****
$*******
*********
 *******
  *****
   ***
    *  
'''
for row in range(5,0,-1):
   
    for col in range(row-1):
        print(" ",end="")
    
    for col in range(row,6):
        print("*",end="")    

    for col in range(row,5):
        print("*",end="")        
    print() 
for row in range(2,6):
   
    for col in range(row-1):
        print(" ",end="")
    
    for col in range(row,6):
        print("*",end="")    

    for col in range(row,5):
        print("*",end="")        
    print()     
print("=================")
'''
5
54
543
5432
54321
'''
for row in range(5,0,-1):
    #               (5,4,-1) 5
    #               (5,3,-1) 54
    #               (5,2,-1) 543
    #               (5,1,-1) 5432
    #               (5,0,-1) 54321 
    for col in range(5,row-1,-1):
        print(col,end="")
    print()    
print("==================")
'''
    5
   54
  543
 5432
54321
'''
for row in range(5,0,-1):
    #space 
    for col in range(row-1):
        print(" ",end="")
    #content
    for col in range(5,row-1,-1):
        print(col,end="")     
    print()    
print("===============")    
'''  
========
A
AB
ABC
ABCD
ABCDE
'''

for a in range(65,70):
    for col in range(65,a+1):
        print(chr(col),end="")
    print()    

'''
==========
    5
   545
  54345
 5432345
543212345
 5432345
  54345
   545
    5       
'''
print("===============")
for row in range(5,0,-1):
    #space 
    for col in range(row-1):
        print(" ",end="")
    #content
    for col in range(5,row-1,-1):
        print(col,end="") 
    #content
    for col in range(row+1,6):
        print(col,end="")       
    print()    
for row in range(2,6):
    #space 
    for col in range(row-1):
        print(" ",end="")
    #content
    for col in range(5,row-1,-1):
        print(col,end="") 
    #content
    for col in range(row+1,6):
        print(col,end="")       
    print()      
print("=================")
'''
    5
   45
  345
 2345
12345    
'''

for row in range(5,0,-1):
    for col in range(row-1):
        print(" ",end="")
    for col in range(row,6):
        print(col,end="")    
    print()    
print("===============")

'''
5
45
345
2345
12345
'''

for row in range(5,0,-1):
    for col in range(row,6):
        print(col,end="")    
    print()    
print("===============")

'''
54321
5432
543
54
5
=====
1
23
456
78910
1112131415
===========
54321
4321
321
21
1
'''
for row in range(5,0,-1):
    for col in range(row,0,-1):
        print(col,end="")
    print()    
'''
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1 
'''


'''
    1
   121
  12312
 1234123
123451234
 1234123
  12312
   121
    1  
============
54321
 4321
  321
   21
    1        
=============
1
23
345
4567
56789 
==============
12345
1234
123
12
1
=========
12345
 1234
  123
   12
    1    
''' 

