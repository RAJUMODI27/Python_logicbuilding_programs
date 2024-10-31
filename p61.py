# Write a program to accept any number and count how many odd digits and how many even digits in that
#  number.

even_count = 0
odd_count = 0

n = int(input("Enter any number: "))

def even_odd(x):
    global even_count, odd_count
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Loop to process each digit in the number
while n > 0:
    last_digit = n % 10
    even_odd(last_digit)
    n = n // 10

# Display the results
print("Even digits count:", even_count)
print("Odd digits count:", odd_count)
