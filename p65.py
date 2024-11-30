# Write a menu driven program which has the following options:
#  a. Factorial of a number.
#  b. Reverse of a number.
#  c. SumofDigits of a number.
#  d. Count Digits of a number.
#  e. Exit.


def menu():
    print("\nChoose an option:")
    print("a. Factorial of a number")
    print("b. Reverse of a number")
    print("c. Sum of digits of a number")
    print("d. Count digits of a number")
    print("e. Exit")

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def reverse_number(num):
    return int(str(num)[::-1])

def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))

def count_digits(num):
    return len(str(abs(num)))

def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case 'a':  # Factorial of a number
                num = int(input("Enter a non-negative integer: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"Factorial of {num} is {factorial(num)}.")
            case 'b':  # Reverse a number
                num = int(input("Enter a number: "))
                print(f"Reverse of {num} is {reverse_number(num)}.")
            case 'c':  # Sum of digits
                num = int(input("Enter a number: "))
                print(f"Sum of digits of {num} is {sum_of_digits(num)}.")
            case 'd':  # Count digits
                num = int(input("Enter a number: "))
                print(f"Count of digits in {num} is {count_digits(num)}.")
            case 'e':  # Exit the program
                print("Exiting the program. Goodbye!")
                break
            case _:  # Handle invalid choice
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
