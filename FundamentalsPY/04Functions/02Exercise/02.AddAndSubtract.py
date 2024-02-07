n1 = int(input())
n2 = int(input())
n3 = int(input())

def sum_numbers(n1, n2):
    total = n1 + n2
    return total
def substract(n3):
    new = sum_numbers(n1, n2) - n3
    return new

print(substract(n3))