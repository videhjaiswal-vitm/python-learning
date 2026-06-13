'''
Logical operator:
&&(and),||(or),!(not)
'''
# c=2<3 and 3>2
# print(c)
# c= 2<=3 and 3>2
# print(c)
# c= 2<=3 and 3<2
# print(c)
# c= 2<2 or 3<2
# print(c)
# c= 2<2 or 3>2
# print(c)
# c= not(2<2) or 3>2
# print(c)
# c= not(2<2) and not(3>2)
# print(c)

c= not(not(2<2) and (3>2))
print(c)