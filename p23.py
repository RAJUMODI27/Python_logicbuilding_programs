# Write a Python Program that accept an integer number and determine whether the inputted number is
# palindrome or not?


x= (input("enter any number"))
isplaindrome=False
palindrom=x[::-1]
if(x==palindrom):
    isplaindrome=True
else:
    isplaindrome=False

print(isplaindrome)