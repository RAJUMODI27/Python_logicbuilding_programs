def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_armstrong(num):
    sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
    return sum_of_cubes == num


def is_perfect(num):
    sum_of_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_of_divisors == num


def is_palindrome(num):
    return str(num) == str(num)[::-1]


while True:
    print("\nMenu:")
    print(" a. Prime or Not")
    print(" b. Armstrong or Not")
    print(" c. Perfect or Not")
    print(" d. Palindrome or Not")
    print(" e. Exit")

    choice = input("Enter your choice: ").lower()

    if choice == 'e':
        print("Exiting program. Goodbye!")
        break
    elif choice in ['a', 'b', 'c', 'd']:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if choice == 'a':
            print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}.")
        elif choice == 'b':
            print(f"{num} is {'an Armstrong number' if is_armstrong(num) else 'Not an Armstrong number'}.")
        elif choice == 'c':
            print(f"{num} is {'a Perfect number' if is_perfect(num) else 'Not a Perfect number'}.")
        elif choice == 'd':
            print(f"{num} is {'a Palindrome' if is_palindrome(num) else 'Not a Palindrome'}.")
    else:
        print("Invalid choice. Please select a valid option.")
