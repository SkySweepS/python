n1 = int(input())
n2 = int(input())
n3 = int(input())

max_n = -100000000
if n1 > max_n:
    max_n = n1
if n2 > max_n:
    max_n = n2
if n3 > max_n:
    max_n = n3

print(max_n)