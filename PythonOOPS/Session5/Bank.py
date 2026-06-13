class Bank:

    customer=""
    balance=0
    accno=0
    savingInterestRate=2.7
    time=0
    si=0
    no_of_customer=0

    def __init__(self,customer,balance,accno,time):
        self.customer=customer
        self.balance=balance
        self.accno=accno
        self.time=time
        Bank.no_of_customer+=1

    def calSavingInterest(self):
        self.si=(self.balance*Bank.savingInterestRate*self.time)/100

    def display(self):
        print("Customer Name is:",self.customer)
        print("Balance in Rs:",self.balance)
        print("Saving Interest Rate is:",Bank.savingInterestRate)
        print("Amount of SI in Rs:",self.si,"in",self.time,"years")
        print("======================")

    @staticmethod
    def BankInfo():
        print("Branch:Vijay Nagar")
        print("Number of Customer:",Bank.no_of_customer)

Bank.savingInterestRate = 3.2

# b1=Bank("Priya Sharma",120000,23223,2)
# b1.calSavingInterest()
# b1.display()

# b2=Bank("Mohan Sharma",420000,45454,5)
# b2.calSavingInterest()
# b2.display()

# b2=Bank("Mohan Sharma",420000,45454,5)
# b2.calSavingInterest()
# b2.display()

# Bank.BankInfo()


'''
Static Variable
1. Create class Book with variable 
title, price.
- Add static variable discountRate.
- Add static variable count. 
Increment count variable by one in 
parameterized initializer.
- Add method to display 
discountRate and count variable.
- Add method to calculateDiscount 
on Book price
enter 4 Book details 
and print sum of all Book prices and sum 
of total discount on all 4 books.
=========================================================================
'''

class Book:
    discountRate=10
    count=0
    def __init__(self,title, price):
        self.title=title
        self.price=price
        Book.count+=1

    def calculateDiscount(self):
        self.discount = (self.price*Book.discountRate)/100    

    def display(self):
        print("Title is:",self.title)
        print("Price in Rs:",self.price)
        print("Discount Rate:",Book.discountRate,"%")
        print("Discount Amount is:",self.discount)
        print("=============")

b1 = Book("C",200)
b2 = Book("C++",200)
b3 = Book("Python",200)
b4 = Book("Core Java",200)
# b1.calculateDiscount()        
# b1.display()

listbook = []
listbook.append(b1)
listbook.append(b2)
listbook.append(b3)
listbook.append(b4)

print(listbook)

print("**************** Book Details *******************")

totalDiscount=0
totalAmount=0
for book in listbook:
    book.calculateDiscount()
    totalDiscount+=book.discount
    totalAmount+=book.price
    book.display() 

print("Total Book Price is:",totalAmount)
print("Total Book Price discount is:",totalDiscount)
print("Number of Book is:",Book.count)
'''
2. Create class Voter with variables 
name,age,address.
- Add static variable votingAge.
- Add method isVoter()->Bool which returns true if age is greater or equal 
than votingAge.
- Add a method to print value of 
votingAge
- Store information of 5 person in 
an array and call isVoter() method on 
all 5 person and print result of 
isVoter().
================================================
1. Create class Student with variable 
(name,course,dateOfBirth)
- create SchoolStudent class with 
variable (fees) and inherit class 
Student
- create CollegeStudent with 
variable(sem and fees) and inherit class 
Student
- create class PGStudent with 
variable(mainSubject, percent) and 
inherit CollegeStudent
-parameterized 
initializer in all classes
==============================================
2. Create class Employee(id,name,salary) 
and add display function
- create class PartTimeEmployee with 
variable(hoursWorked , hourlyRate) and 
inherit 
- class Employee. Add 
calculateSalary() function to calcualte 
salary as
salary = hourlyRate * hoursWorked
- create class FullTimeEmployee with 
variables(basic,da,pf) and Add 
calculateSalary() function to calcualte 
salary as
salary = basic + da - pf
- add default and parameterized 
initializer in all classes
- Create a global function getTax() 
which accept Employee object in argument 
and calculate and print income tax on 
employee salary(12.5% of salary)
- Also try to pass Objects of 
PartTimeEmployee and FullTimeEmployee to 
getTax() method
'''











