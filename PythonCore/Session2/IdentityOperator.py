'''
Identity Operator:
is , is not
'''

a=10
print("a is:",a,"Memory address is:",id(a))
b=10
print("b is:",b,"Memory address is:",id(b))

r = a is b 
print(r)
r = a is not b 
print(r)
print("==============")
a=10
print("a is:",a,"Memory address is:",id(a))
b=20
print("b is:",b,"Memory address is:",id(b))

r = a is b 
print(r)
r = a is not b 
print(r)