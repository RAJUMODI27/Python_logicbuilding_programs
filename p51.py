# Write a Python Program to do the addition of the first n terms of the fibonacci series.
count=5


def fibonacci_sum(n):
    a, b = 0, 1
    total_sum = 0

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        total_sum += a
        a, b = b, a + b

    print(f"\nSum of the first {n} terms: {total_sum}")



count=int(input("Enter total nuber of fibbo terms"))
fibonacci_sum(count)
