'''
Q.1 Write a program accepts two numbers from user and calculates first no is divisible by second or not.
==================
first = int(input("Enter a First Number\n"))
second = int(input("Enter a Second Number\n"))

if first%second==0:
    print(first,"is Divisible by",second)
else:
    print(first,"is not Divisible by",second)    
===============================
Q.5 Write a program accepts a three digit number from user and check given number is palindrome number or not. 

num=int(input("Enter a three digit number\n"))
temp=num
rev=0
rem=num%10 #3
rev=rev*10+rem #0*10+3=3
num=num//10 #12

rem=num%10 #2
rev=rev*10+rem #3*10+2=32
num=num//10 #1

rem=num%10 #1
rev=rev*10+rem #32*10+1=321
num=num//10 #0

print("Reverse is :",rev)

if temp==rev:
   print("Palindrome number")
else:
   print("Not a Palindrome number")    
===============
Q.6 Write a program accepts a three digit number from user and check given number is Armstrong number or not. 
ex:371 = 3 power of 3 + 7 power of 3 + 1 power of 3
       = 27 + 343 + 1
       = 371
=======================   
'''
num=372
temp=num
sum=0

rem=num%10 #1
sum=sum+rem**3 #0+1=1
num=num//10 #37

rem=num%10 #7
sum=sum+rem**3 #1+343=344
num=num//10 #3

rem=num%10 #3
sum=sum+rem**3 #344+27=371
num=num//10 #0

print("Sum is:",sum)

if sum==temp:
   print("Armstrong Number")
else:
   print("Not an Armstrong Number")    
#======================
'''
Q.14 Write a program for generating electricity Bill Accept last month unit and current month unit from user, then calculate and print bill amount according to following condition 
0-150 charges 4 rs/unit 
151-300 charges 6 rs/unit 
301-500 8rs/unit 
>500 charges 10rs/unit.
'''
current_month = int(input("Enter a current month unit\n"))
last_month = int(input("Enter a last month unit \n"))
total_unit = current_month - last_month
electricity_bill=0 
if total_unit>0 and total_unit<=150 :
   electricity_bill=total_unit*4 
elif total_unit>150 and total_unit<=300: 
   electricity_bill=total_unit*6
elif total_unit>300 and total_unit<=500: 
   electricity_bill=total_unit*8
else:
   electricity_bill=total_unit*10
print("Bill amount is:",electricity_bill)
   




