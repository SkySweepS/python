n1 = int(input())
n2 = int(input())
nn1 = n1 % 10
nn2 = n2 % 10
n_11 = (n1 // 10) % 10
n_101 = n1 // 100 % 10
n_1001 = n1 // 1000 % 10
n_12 = n2 // 10 % 10
n_102 = n2 // 100 % 10
n_1002 = n2 // 1000 % 10

#print(n_11)
#print(n_12)
#print(n_101)
#print(n_102)
#print(n_1001)
#print(n_1002)
for i in range(*sorted([nn1, nn2 + 1])):
    if i % 2 == 1:
        for i1 in range(*sorted([n_11, n_12 + 1])):
            if i1 % 2 == 1:
                for i2 in range(*sorted([n_101, n_102 + 1])):
                    if i2 % 2 == 1:
                        for i3 in range(*sorted([n_1001, n_1002 + 1])):
                             if i3 % 2 == 1:
                                print(f"{i3}{i2}{i1}{i}")