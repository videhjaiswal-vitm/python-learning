# 4.A cashier has some amount of money (eg 4567).Write a program to calculate how many currency of Rs2000, Rs500,Rs 200, Rs100, Rs50, Rs20, Rs10, Rs5 ,Rs2 ,Rs1.

amt=5888
note2000=0
note2000=amt//2000 #2
amt=amt%2000 #567
print("Note2000 Count is:",note2000)
print("Remaining Amount is:",amt)
#==============
note500=0
note500=amt//500 #1
amt=amt%500 #67
print("Note500 Count is:",note500)
print("Remaining Amount is:",amt)
#==============
note200=0
note200=amt//200 #0
amt=amt%200 #67
print("Note200 Count is:",note200)
print("Remaining Amount is:",amt)
#==============
note100=0
note100=amt//100 #0
amt=amt%100 #67
print("Note100 Count is:",note100)
print("Remaining Amount is:",amt)
#==============
note50=0
note50=amt//50 #1
amt=amt%50 #17
print("Note50 Count is:",note50)
print("Remaining Amount is:",amt)
#==============
note20=0
note20=amt//20 #0
amt=amt%20 #17
print("Note20 Count is:",note20)
print("Remaining Amount is:",amt)
#==============
note10=0
note10=amt//10 #1
amt=amt%10 #7
print("Note10 Count is:",note10)
print("Remaining Amount is:",amt)
#==============
note5=0
note5=amt//5 #1
amt=amt%5 #2
print("Note5 Count is:",note5)
print("Remaining Amount is:",amt)
#==============
note2=0
note2=amt//2 #1
amt=amt%2 #0
print("Note2 Count is:",note2)
print("Remaining Amount is:",amt)
#==============
note1=0
note1=amt//1 #0
amt=amt%1 #0
print("Note1 Count is:",note1)
print("Remaining Amount is:",amt)
