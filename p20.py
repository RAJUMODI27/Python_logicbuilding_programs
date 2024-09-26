# Function to check if a number is an Armstrong number
def is_armstrong(num):
    num_str = str(num)
    length = len(num_str)
    armstrong_sum = 0

    for digit in num_str:
        armstrong_sum += int(digit) ** length

    return num == armstrong_sum


for num in range(1, 501):
    if is_armstrong(num):
        print(num)
