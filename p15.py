# Given number is armstrong or not
n=int(input("Enter ny number "))

tot=0
qube_tot=0
no_digit=len(str(n))
org=n
while(n>0):
    rem=n%10
    qube_tot=qube_tot+(rem**no_digit)
    n=n//10
if(qube_tot==org):
    print("armnstrong ")


