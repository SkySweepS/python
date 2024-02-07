n = int(input())
def bar(n):

    num = n // 10
    list_1 = []
    for i in range(1, num + 1):
        list_1.append("%")
    for i1 in range(1, 10 - num + 1):
        list_1.append(".")
    bar_string = "".join(list_1)
    return bar_string

if n == 100:
    print(f"{n}% Complete!")
    print(f"[{bar(n)}]")
elif n < 100:
    print(f"{n}% [{bar(n)}]")
    print("Still loading...")