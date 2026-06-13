'''
String:It is a sequence which is used to store multiple characters,numbers,alphanumeric data where each element is given by integer index value which is used to access and manage data.
Note:It is immutable.
'''
s1 = "rahul sharma"
#+ve  012345678910
#-ve        -3-2-1  
print(s1)
print(type(s1))
print("================")

#access single data
print("s1[3]:",s1[3])
print("s1[-3]:",s1[-3])
print("================")
#access all data with +ve index
for index in range(len(s1)):
    print("Index:",index,"Data:",s1[index])
print("================")

#access all data with -ve index
for index in range(-len(s1),0):
    print("Index:",index,"Data:",s1[index])
print("================")

#access all data without index
for d in s1:
    print(d,end="")
print()     
print("========")

#find vowels in a string
print(s1)
print("Vowel is:")  
count=0
for ch in s1:
    #print(ch)
    if ch in "aeiou":
       print(ch,end="")
       count+=1
print()    

print("Count is:",count)
#======

#concatenation +
fn="mohan"
ln="verma"
age=32
r=fn+" "+ln+" "+str(age)
print(r)
print("============")
#multiplier *
n="priya "
r=n*5
print(r)
print("===============")

a,b,c="red","green","blue"
print("Max:",max(a,b,c))
print("Min:",min(a,b,c))

print("===============")

#case conversion
s1="rahul sharma"
print("Upper Case:",s1.upper())
print("Lower Case:",s1.lower())
print("Title Case:",s1.title())
print("Capitalize Case:",s1.capitalize())
print("===============")

s1=" "
print("Is Upper Case:",s1.isupper())
print("Is Lower Case:",s1.islower())
print("Is Title Case:",s1.istitle())
print("Is Numeric Case:",s1.isnumeric())
print("Is Alphanumric Case:",s1.isalnum())
print("Is Alphabet Case:",s1.isalpha())
print("Is isSpace Case:",s1.isspace())
print("===============")

s1="rahul sharma"
#slice(stop)
obj=slice(3)
print("s1[3]:",s1[obj])
obj=slice(1,6)
print("s1[1,6]:",s1[obj])
obj=slice(1,8,2)
print("s1[1,8,2]:",s1[obj]) #au h
obj=slice(-8,-1)
print("s1[-8,-1]:",s1[obj]) #
obj=slice(-8,-1,2)
print("s1[-8,-1,2]:",s1[obj]) #
print("=========================")

s1="Shashwat is a good boy,good in cricket and also good in singing"
newstring=s1.replace("good","best",2)
print(s1)
print(newstring)
print("=========================")

names="Raju$Shayam$Babu$Mohan$Sonam$Priya"
print(names)
nameslist=names.split("$")
print(nameslist)
for name in nameslist:
    print(name)
print("=========================")

s1="mohan sharma"
print(s1)
print("Reverse string:",s1[::-1])
print("=========================")

l1=[10,20,30,40,50]
#   0  1   2  3 4 
#   50 40 30 20 10    
print("Before Reverse:")
for index in range(len(l1)):
    print("index:",index,"data:",l1[index])
print("============")
#logic
# counter=len(l1)-1
# for index in range(len(l1)//2):
#     temp=l1[index]
#     l1[index]=l1[counter]
#     l1[counter]=temp
#     counter-=1 
l1.reverse()
print("After Reverse:")
for index in range(len(l1)):
    print("index:",index,"data:",l1[index])


















