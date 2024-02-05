import math

num_list = input().split(" ")
remove_count = int(input())
n = []
for i in num_list:
    n.append(int(i))
n.sort(reverse=True)
num = []
for i in range(remove_count):

    n.pop(-1)
num = [] * len(n)
for i in n:
    num.append(str(i))
new_list = [] * len(n)
for i in num_list:
    if i in num:
        new_list.append(str(i))
print(", ".join(new_list))
#print(" ".join(num))
#print(num_list)
