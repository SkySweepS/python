numbers = input().split(" ")

def even(n):
    num = []
    for i in n:
        if int(i) % 2 == 0:
            num.append(int(i))
    return num

print(even(numbers))
