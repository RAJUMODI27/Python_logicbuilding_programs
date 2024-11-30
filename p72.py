num = 1
for i in range(1, 6):
    for j in range(num, num + i):
        print(j, end=" ")
    print()
    num = num + i
