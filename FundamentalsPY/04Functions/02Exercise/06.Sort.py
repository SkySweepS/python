numbers = input().split(" ")

def sor(n):
    new = []
    for i in n:
        new.append(int(i))
    new = sorted(new)
    return new

print(sor(numbers))