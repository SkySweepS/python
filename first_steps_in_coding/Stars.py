n = int(input())

for i in range(0, n):
    print("*" * n)
for i in range(1, n - 1):
    print("*" + " " * (n - 2) + "*")
print("*"*n)
