# Write a menu driven program which has the following options:
#  a. Positive or Negative.
#  b. Even or Odd.
#  c. Leap Year or Not Leap Year.
#  d. Maximum of two numbers.
#  e. Exit.
#  Make use of SWITCH statement.




def menu():
    print("\nChoose an option:")
    print("a. Positive or Negative")
    print("b. Even or Odd")
    print("c. Leap Year or Not Leap Year")
    print("d. Maximum of two numbers")
    print("e. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip().lower()
        match choice:
            case 'a':  # Check Positive or Negative
                num = float(input("Enter a number: "))
                if num > 0:
                    print(f"{num} is Positive.")
                elif num < 0:
                    print(f"{num} is Negative.")
                else:
                    print(f"{num} is Zero (neither positive nor negative).")
            case 'b':  # Check Even or Odd
                num = int(input("Enter an integer: "))
                if num % 2 == 0:
                    print(f"{num} is Even.")
                else:
                    print(f"{num} is Odd.")
            case 'c':  # Check Leap Year
                year = int(input("Enter a year: "))
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    print(f"{year} is a Leap Year.")
                else:
                    print(f"{year} is not a Leap Year.")
            case 'd':  # Find Maximum of Two Numbers
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                max_num = max(num1, num2)
                print(f"The maximum of {num1} and {num2} is {max_num}.")
            case 'e':  # Exit the Program
                print("Exiting the program. Goodbye!")
                break
            case _:  # Handle Invalid Choice
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
