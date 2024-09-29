def generate_series(n):
    series = [2, 3]

    while len(series) < n:
        next_term = series[-1] + series[-2]
        series.append(next_term)

    return series



n = int(input("Enter the number of terms: "))


result = generate_series(n)
print("Series:", ' '.join(map(str, result)))
