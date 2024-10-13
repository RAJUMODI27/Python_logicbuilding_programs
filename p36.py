# Write a Python Program to Calculate the sum of first 25 prime numbers. ( Result = 101 )

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if((n%i)==0):
            return False
    return True



c=0
n=2
total_prim=0
while(c<25):
    if(isprime(n)):
        c+=1
        print(n,"\n")
        total_prim+=n
    n+=1
print(total_prim)