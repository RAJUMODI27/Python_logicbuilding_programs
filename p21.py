# Write a program and to accept any integer number and print the individual number in
# words. For ex. Input - 546 Output – Five Four Six



def number_to_words(num):
    words = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }

    num_str = str(num)
    result = []

    for digit in num_str:
        result.append(words[digit])

    return ' '.join(result)


input_number = int(input("Enter an integer number: "))
output = number_to_words(input_number)
print(output)
