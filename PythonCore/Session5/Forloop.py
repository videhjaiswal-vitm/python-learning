'''
for loop:It will not be infinity
---------
Syntax:
for variablename in range(stop):
    statement...
'''
#print Hello World five times
for a in range(5):
    print("Hello World:",a)
print("===================")    
for a in range(5):
    print(a,end=" ")
print()    
print("===================")    
for a in range(1,7):
    print(a,end=" ")
print()    
print("===================")    
for a in range(1,7,2):
    print(a,end=" ")
print()    
print("===================") 
for a in range(10,0,-1):
    print(a,end=" ")
print()    
print("===================") 
for a in range(10,0,-2):
    print(a,end=" ")
print()    
print("===================") 

'''
Q.6 Write a program that accepts a number from user and check given number is palindrome number or not. 


num=int(input("Enter a number\n"))
temp=num
rev=0
for a in range(num):
    if num!=0:
        rem=num%10
        rev=rev*10+rem
        num=num//10

print("Reverse is:",rev)

if temp==rev:
   print("Palindrome number")
else:
   print("Not a Palindrome number")
'''
'''
Q.9 Write a program that accepts a number from user check given number is perfect number or not. 
6=1+2+3=6
num=6
sum=0
for a in range(1,num):
    if num%a==0:
       sum=sum+a
print("sum is:",sum)
if sum==num:
   print("Perfect Number")
else:
   print("Not a Perfect Number")
======
Q.10 Write a program that accepts a number from user check given number is strong number or not. 
145=1!+4!+5!
   =1+24+120
   =145 


num=40585
temp=num
count=0
while num!=0:
    count+=1
    num=num//10
print("Count is:",count)    

num=temp
sum=0
while num!=0:
    rem=num%10 #5
    f=1
    for a in range(rem,0,-1):
        f=f*a
    print("Factorial of :",rem,"is:",f)
    sum=sum+f 
    num=num//10
print("Sum is:",sum)

if sum==temp:
   print("Strong Number")
else:
    print("Not a Strong Number")   

==========================
print("Strong Number:")
x=1
while x<=100000:
    #===============
    num=x
    temp=num
    count=0
    while num!=0:
        count+=1
        num=num//10
    #print("Count is:",count)    

    num=temp
    sum=0
    while num!=0:
        rem=num%10 #5
        f=1
        for a in range(rem,0,-1):
            f=f*a
        #print("Factorial of :",rem,"is:",f)
        sum=sum+f 
        num=num//10
    #print("Sum is:",sum)

    if sum==temp:
       print(sum)
    #===============
    x+=1
'''
'''
Q.16 Write a program that accepts a number from user and check given number is prime number or not.
for a in range(2,2): #false
    print("hello")
else:
    print("hi")
'''
num=int(input("Enter a number\n"))
temp=1
for a in range(2,num):
    if num%a==0:
       temp=0
       break
    
if temp==0:
    print("Not a Prime Number:",num)    
else:
    print("Prime Number:",num)
