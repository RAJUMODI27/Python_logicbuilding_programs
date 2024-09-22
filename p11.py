# 1, 2, 4, 7, 11, 16

n = 1
diff = 1
terms = 10

for i in range(terms):
    print(n, end=" ")
    n = n + diff
    diff = diff + 1
