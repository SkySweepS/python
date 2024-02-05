string = input().split()
#print(string)
num_list = []
for num in string:
    n = int(num)
    if n > 0:
        num_list.append(int(0 - n))
    else:
        num_list.append(int(0 + abs(n)))
print(num_list)

