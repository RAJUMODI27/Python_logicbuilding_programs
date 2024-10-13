# Write a Python Program to Calculate the Series like 1-2+3-4…. –10 (Result = -5)
from functools import reduce
l=[]
def addtolist(n):
    l.append(n)

for i in range(1,11):
    if(i%2==0):
        addtolist(-i)
    else:
        addtolist(i)

x=reduce(lambda x,y:x+y,l)
print(x)