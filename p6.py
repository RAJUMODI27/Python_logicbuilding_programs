# Write a Python Program to print n to 1 even numbers
n=int(input("Enter any number \n"))
x=n
while(x>1):
    if(x%2==0):
        print(x)
    x-=1