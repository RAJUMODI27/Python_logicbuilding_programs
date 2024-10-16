#  Write a Python Program to check whether the given number is perfect (or magic)
# or not. A number is perfect if its sum of digits is same as multiplication of digit.
# (e.g. 123 is perfect no. because 1+2+3 = 1*2*3)


lhs=0
rhs=1

add=0
mul=0

n=1234
rev=0
while(n>0):
    rem=n%10
    lhs+=rem
    rhs*=rem
    n//=10
if(lhs==rhs):
    print("its magic no")
else:
    print("its not magic no")
