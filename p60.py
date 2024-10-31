def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

fibonacci = [0, 1]
while len(fibonacci) < 20:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

prime_fibonacci = [num for num in fibonacci if is_prime(num)]
print("First 10 prime Fibonacci numbers:", prime_fibonacci[:10])
