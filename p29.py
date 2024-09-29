# 29 Display the following series :
# # 1 2 2 4 8 32 256 up to a given range



def generate_series(n):
    series = [1, 2]

    for i in range(2, n):
        next_term = series[-1] * series[-2]
        series.append(next_term)

    return series



n = int(input("Enter the number of terms: "))


result = generate_series(n)
print(*result)
