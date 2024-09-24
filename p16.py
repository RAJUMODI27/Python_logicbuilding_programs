# find factorial of number

n=int(input("enter the any number to find factorial"))
f=1

while(n>=1):
    f*=n
    n-=1
print(f)