# Write a Python Program to Calculate the sum of fist 50 odd numbers. ( Result = 625 )

def isodd(n):
    if(n%2==0):
        return False
    return True


oddtotal=0

for i in range(50):
    if(isodd(i)):
        oddtotal+=i;

print(oddtotal)
