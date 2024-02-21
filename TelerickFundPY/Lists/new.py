n = int(input())
list_n = []
max_num = []
list_len = []
for i in range(n):
    num = int(input())
    list_n.append(int(num))
for i in range(len(list_n)):
    if list_n[i] % 2 == 1:
        list_len = []
    else:
        list_len.append(list_n[i])
    if len(list_len) > len(max_num):
        max_num = list_len


print(len(max_num))
