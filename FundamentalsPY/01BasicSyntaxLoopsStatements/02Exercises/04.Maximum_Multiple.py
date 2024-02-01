divisor = int(input())
boundary = int(input())

max_n = -10000000
for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > max_n:
            max_n = i

print(max_n)
