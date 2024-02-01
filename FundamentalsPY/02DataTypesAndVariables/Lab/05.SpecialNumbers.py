n = int(input())

for i in range(1, n + 1):
    summ = 0
    for num in str(i):
        summ += int(num)
        special = summ == 5 or summ == 7 or sum == 11
    print(f"{i} -> {special}")
    