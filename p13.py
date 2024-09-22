# Write a program to read any number and print the sum of all values.

x=int(input("enter any number\n"))
temp=0


while(x>0):
    ls = x % 10
    temp = temp + ls
    x = x // 10
print(temp)