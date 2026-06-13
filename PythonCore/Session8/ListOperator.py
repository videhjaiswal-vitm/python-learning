'''
List Operator:
'''
#+ concatenation
l1=[10,20,30,40,50]
l2=[60,70,80,90,100]
l=l1+l2
print(l)
print("================")

#* multiplier
l=[1,2,3,4,5]
r=l*5
print(r)
print("================")

#membership operator:in , not in
l=[10,20,30,40,50]
val=20
r=val in l 
print(r)
r=val not in l 
print(r)
print("================")

#range slice
#range[start:stop:step] 
l=[10,20,30,40,50,60,70,80,90,100]
print(l[:5])
print(l[1:5])
print(l[1:9:2])
print(l[-6:-2])
print(l[-8:-2:2])
print(l[1:])
print(l[1:5:3])