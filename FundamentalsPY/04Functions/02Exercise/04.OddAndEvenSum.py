number = input()

def sum(n):
    even = 0
    odd = 0
    for i in n:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    print(f"Odd sum = {odd}, Even sum = {even}")

sum(number)