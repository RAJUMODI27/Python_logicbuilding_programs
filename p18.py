# write a python program to generate series 1/2!+2/3!.. 10 terms



def fact(n):
    f = 1
    while (n >= 1):
        f *= n
        n -= 1
    return f

def series_sum():
    total_sum = 0
    for i in range(1, 11):
        total_sum += i / fact(i+1)
    return total_sum

result = series_sum()
print(result)
