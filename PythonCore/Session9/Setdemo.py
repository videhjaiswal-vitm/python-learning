'''
Set: It is a built-in datatype in python which is used to store hetergenous data but their is no index value.
1.no duplicate value.
2.mutable
3.random order
Syntax:
setname = {e1,e2,....en}
'''

setdemo = {"g","o","o","g","l","e"}
print(setdemo)
print(type(setdemo))
print("==============")

#access all data
for data in setdemo:
    print(data)
print("==============")

#add data
setdemo.add("a")
setdemo.add("b")
setdemo.add("c")
print(setdemo)

#merge two set
s1 = {10,20,30,40,50}
s2 = {60,70,80,90,100}
s1.update(s2)
print(s1)

#remove data
setdemo.discard("a")
setdemo.discard("b")
setdemo.discard("c")
print(setdemo)

#empty
setdemo.clear()
print(setdemo)





















































