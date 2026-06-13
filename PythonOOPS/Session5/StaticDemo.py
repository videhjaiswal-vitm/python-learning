'''
Static Variable:
1.Single memory allocation.
2.Access via classname.
3.All objects of a class share memory of a static or class variable.
'''

class Example:
    #class variable
    counter=0
    count=0

    def increment(self):
        self.count+=1
        Example.counter+=1
        print("Counter is:",Example.counter)
        # print("Count is:",self.count)

Example().increment() #0+1=1
Example().increment() #1+1=2
Example().increment() #2+1=3
Example().increment() #3+1=4
Example().increment() #4+1=5


