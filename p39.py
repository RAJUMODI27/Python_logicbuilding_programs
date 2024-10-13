# Write a Python Program to Calculate the Series like 1/2 + 2/3 + 3/4 + …+9/10 (Result = 7.071)


c=0
for i in range(1,10):
    c=c+i/(i+1)
print(c)
