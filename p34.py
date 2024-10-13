# Write a program to generate series like 2 5 10 17 26………..n (Square + 1 Series)


# n=10
l=[]
def series(n):
    a = 2

    while(n>0):
        x=a**2+1
        l.append(x)
        n-=1
        a+=1

series(5)
print(l)