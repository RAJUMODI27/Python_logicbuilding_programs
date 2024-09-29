# Input any number in decimal form and print it in Binary, octal and hexadecimal form

decimal_number = int(input("Enter a decimal number: "))

binary_form = bin(decimal_number)
octal_form = oct(decimal_number)
hexadecimal_form = hex(decimal_number)

# Print the results
print(f"Binary form: {binary_form[2:]}")
print(f"Octal form: {octal_form[2:]}")
print(f"Hexadecimal form: {hexadecimal_form[2:]}")
