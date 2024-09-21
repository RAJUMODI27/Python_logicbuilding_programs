# Write a Python Program to print 1 to n even numbers

n=int(input("Enter any number \n"))
x=1
while(x<n):
    if(x%2==0):
        print(x)
    x+=1