# first  n term in fibonnaci

terms=int(input("enter terms"))

a=1
b=1
c=0
print(a)
print(b)

while(terms-2>0):
    c=a+b
    print(c)
    a=b
    b=c
    terms-=1
