# Write a menu driven program which has the following options:
#  a. Addition of 2 numbers
#  b. Subtraction of 2 numbers
#  c. Multiplication of 2 numbers
#  d. Division of 2 numbers
#  e. Exit.
#  Make use of SWITCH statement.



def menu():
    print("\nChoose an option:")
    print("a. Addition of 2 numbers")
    print("b. Subtraction of 2 numbers")
    print("c. Multiplication of 2 numbers")
    print("d. Division of 2 numbers")
    print("e. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case 'a':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"Result: {num1 + num2}")
            case 'b':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"Result: {num1 - num2}")
            case 'c':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"Result: {num1 * num2}")
            case 'd':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Division by zero is not allowed.")
            case 'e':
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
