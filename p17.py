# 1!+2!+3!+4!+5!

n=int(input("enter the number \n"))
fact=1
tot_fact=0

for i in range(1,n+1):
    fact=1
    while(i>=1):
        fact*=i
        i-=1
    tot_fact+=fact
print(tot_fact)