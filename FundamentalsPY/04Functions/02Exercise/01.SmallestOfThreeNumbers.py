my_list = []
n1 = int(input())
n2 = int(input())
n3 = int(input())
my_list.append(n1)
my_list.append(n2)
my_list.append(n3)

def smallest(n1):
    n1.sort()
    value = n1[0]
    return value


print(smallest(my_list))