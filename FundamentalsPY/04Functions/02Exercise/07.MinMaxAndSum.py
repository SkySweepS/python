numbers = input().split(" ")

def min_numbers(n):
    sortt = []
    for i in n:
        sortt.append(int(i))
    sort = sorted(sortt)
    return sort[0]
def max_numbers(n1):
    sortt = []
    for i in n1:
        sortt.append(int(i))
    sort = sorted(sortt)
    return sort[-1]
def sum_numbers(n2):
    sum = 0
    for i in n2:
        sum += int(i)
    return sum

print(f"The minimum number is {min_numbers(numbers)}")
print(f"The maximum number is {max_numbers(numbers)}")
print(f"The sum number is: {sum_numbers(numbers)}")

