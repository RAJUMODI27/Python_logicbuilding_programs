# Write a program to print first 10 numbers of fibonacci series, which are prime numbers

isprime=False



def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if (x % i == 0):
            return False
    return True



def fibannico():
    primeTot = 0

    a = 1
    b = 1
    c = 0
    while (primeTot<=10):
        c = a + b
        a = b
        b = c
        if (prime(c)):
            print(c)
            primeTot += 1



fibannico()


