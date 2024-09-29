#  Write a program to take an integer and find the sum of first and last digit.
# Ex. Input: 1234
# Output: 5



n=(input("enter any number"))
last=n[-1]
last_digit_append=int(last)+1
n=n + str(last_digit_append)
print(n)