'''
File Handling:It is a permanent storage which is used to store bulk amount of data simulateneously at particular location. 
Once created, they can also be accessed and managed manually.
Syntax:
open("filepath","mode")

mode:
1. w(write): It checks if file exists or not.If not exists then,
it will create a file and content can be written, if exists, then it will override file content.
-----
2.a(append): It checks if file exists or not.If not exists then,
it will create a file and content can be written,if exists, then it will update file content.
-----
3.r(read): It checks if file exists or not. If not exists, it will result a error, if exists, it will read file content.
==========================
Binary Mode:
1. wb(write binary): It checks if file exists or not.If not exists then,
it will create a file and content can be written, if exists, then it will override file content.
----------
2.ab(append binary): It checks if file exists or not.If not exists then,
it will create a file and content can be written,if exists, then it will update file content.
----------
3.rb(read binary):It checks if file exists or not. If not exists, it will result a error, if exists, it will read file content.
--------
fo=open("demo.txt","w")
print("File Path:",fo.name)
print("File Mode:",fo.mode)
print("Is File is Closed:",fo.closed)
fo.close()
print("Is File is Closed:",fo.closed)
============
fo=open("demo.txt","w")
content = "Good Afternoon"
fo.write(content)
print("Written Content Successfully!!")
=============
fo=open("demo.txt","a")
content = " How are you today?"
fo.write(content)
print("Apend Content Successfully!!")
===============
fo=open("demo.txt","r")
strdata = fo.read()
print(strdata)
print("Read Content Successfully")
print("=================================")
fo=open("demo.txt","r")
strdata = fo.read(20)
print(strdata)
print("Read Content Successfully")
print("=================================")
'''
# fo=open("demo.txt","r")
# strdata = fo.read()
# print(strdata)

# fo=open("demo.txt","r")
# print("Position 1:",fo.tell())
# strdata = fo.read(20)
# print(strdata)
# print("Position 2:",fo.tell())
# strdata = fo.read(20)
# print(strdata)
# print("Position 3:",fo.tell())
# strdata = fo.read(15)
# print(strdata)
# print("Position 4:",fo.tell())

fo=open("demo.txt","r")
strdata = fo.read()
print(strdata)
print("Position 1:",fo.tell())
fo.seek(10)
print("Position 2:",fo.tell())
strdata = fo.read(10)
print(strdata)
print("Position 3:",fo.tell())
