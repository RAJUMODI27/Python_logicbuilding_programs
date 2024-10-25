# Write a program to find first N prime number.
import math


def is_prime(num):
    if num < 2:
        return False
    for j in range(2, int(math.sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True


def find_primes(n):
    primes = []
    i = 2

    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1

    return primes



n = int(input("Enter the number of prime numbers to find: "))
primes_list = find_primes(n)
print(f"The first {n} prime numbers are: {primes_list}")
