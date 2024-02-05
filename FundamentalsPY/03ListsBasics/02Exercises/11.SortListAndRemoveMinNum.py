import math

num_list = input().split(" ")
remove_count = int(input())
n = []
for i in num_list:
    n.append(int(i))
n.sort(reverse=True)

for i in range(remove_count):

    n.pop(-1)
print(n)
