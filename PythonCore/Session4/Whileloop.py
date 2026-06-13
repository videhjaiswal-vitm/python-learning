'''
loop:repitation
Syntax:
while condition:
    statement 
'''

#Print Hello World Five times
a=1
while a<=5:
    print("Hello World:",a)
    a+=1
print("=============")
#Print Hello World Five times
#a=6

while a>1:
    a-=1
    print("Hello World:",a)
print("=============")

#find sum of squares of a number from 1 to 5
#1+4+9+16+25=55
a=1
sum=0
while a<=5:
    sum=sum+a*a
    #sum=0+1*1=1
    #sum=1+2*2=5
    #sum=5+3*3=14
    #sum=14+4*4=30
    #sum=30+5*5=55     
    #sum+=a*a
    a+=1
print("Sum is:",sum)    
#print table from a given number
# 5x1=5
# 5x2=10
# ...
# 5x10=50

a=1
t=5
while a<=10:
    print(t,"x",a,"=",t*a)
    a+=1
#palindrome number 
#1234 4321
#1221 1221

num=int(input("Enter a number\n"))
temp=num
rev=0
while num!=0:
    rem=num%10 
    rev=rev*10+rem 
    num=num//10
print("Reverse is :",rev)
if temp==rev:
   print("Palindrome number")
else:
   print("Not a Palindrome number") 

'''
Q.1 Write a program to print n natural number. 
Q.2 Write a program to calculate factorial of given number. 
Q.3 Write a program to calculate square from 1-10 numbers. 
Q.4 Write a program to print table of any given numbers. 
Q.5 Write a program to find out reverse of a given number. 
Q.6 Write a program that accepts a number from user and check given number is palindrome number 
or not. 
Q.7 Write a program that accepts a number from user and check given number is Armstrong number or not. 
Q.8 Write a program that accepts a number from user calculate factor of a given number. 
Q.9 Write a program that accepts a number from user check given number is perfect number or not. 
Q.10 Write a program to print Fibonacci Series. 
Q.11 Write a program to calculate sum of digits of a number. 
Q.12 Write a program to calculate sum of squares of n natural number. 
Q.13 Write a program to accept n number from user and show how many number are even or odd. 
Q.14 Write a program to find LCM of two numbers. 
Q.15 Write a program to find HCF of two numbers. 
Q.16 Write a program that accepts a number from user and check given number is prime number or not.
'''










