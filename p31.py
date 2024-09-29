# Calculate the sum of first n odd integers (i.e. 1+3+5..+2n-1)

n=int(input("enter toal number of terms"))
isodd=False
o=1

x=[]

while(n>0):
    if(o%2!=0):
        x.append(o)
    o+=1
    n-=1
print(x)
