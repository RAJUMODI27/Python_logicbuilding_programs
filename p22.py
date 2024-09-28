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

    result.reverse()

    return ' '.join(result)


input_number = int(input("Enter an integer number: "))
output = number_to_words(input_number)
print(output)
