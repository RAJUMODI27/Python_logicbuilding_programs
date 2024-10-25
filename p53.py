# generate following series 2, 3, 5, 9, 17, 33, 65

count = 20
a = 2
b = 3

l = [a, b]
i = 0

while len(l) < count:
    n = l[i] * l[i + 1] - 1
    l.append(n)
    i += 1

print(l)

