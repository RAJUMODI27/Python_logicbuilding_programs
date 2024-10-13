# Write a Python Program to Calculate the series like 1+2+3…+10 ( Result = 55 )
from functools import  reduce
x=reduce(lambda x,y:x+y,range(1,11))
print(x)