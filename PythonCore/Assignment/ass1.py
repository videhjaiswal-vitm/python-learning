# 3.Write a program that accepts a three digit number and obtain reverse of a number.

num=int(input("Enter a three digit number\n"))
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
