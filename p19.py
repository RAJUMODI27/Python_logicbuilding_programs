# Write a Python Program to generate the following
# output1+2+3+4+5+6+7+8+9+10=55

n=int(input("enter any number"))
i=1
tot=0
st=""
while(i<=n):
    tot+=n
    st+=f"{i}"
    if(i<n):
        st+="+"
    else:
        st+="="
    i+=1
print(st,tot)
