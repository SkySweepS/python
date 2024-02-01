n = int(input())
for i in range(1, n + 1):
    for i1 in range(0, i):
        print("*", end="")
    print()
for i2 in range(n - 1, 0, -1):
    for i3 in range(0, i2):
        print("*", end="")
    print()
