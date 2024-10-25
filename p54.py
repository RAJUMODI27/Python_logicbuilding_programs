n=10

x=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j**x+1,end="")
        x+=1
    print("\n")