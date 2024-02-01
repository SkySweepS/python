str_one = input()
str_two = input()

for i in range(len(str_one)):
    if str_one[i] != str_two[i]:
        for i1 in range(0, i + 1):
            print(str_two[i1], end="")

        for i2 in range(i + 1, len(str_one)):
            print(str_one[i2], end="")
        print()
