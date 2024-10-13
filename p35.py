# Write a Python Program to Calculate a Series like 1 / 1! + 2 / 2! + + 10 / 10!
import math


def series(n):
    x=0
    while(n>0):
        x=x+n/math.factorial(n)
        n-=1
    return x
print(series(10))