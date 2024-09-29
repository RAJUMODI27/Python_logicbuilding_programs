# Write a program to find first N prime number.

terms = int(input("Enter the total primes to find"))
prime = []
num = 2

while len(prime) < terms:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime.append(num)

    num += 1

print(prime)
