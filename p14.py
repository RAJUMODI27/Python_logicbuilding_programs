 # Write a program to determine whether a number is prime or not.
n=int(input("enter the number "))


for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        print("Not prime")
        break
    else:
        print("prime")
        break

