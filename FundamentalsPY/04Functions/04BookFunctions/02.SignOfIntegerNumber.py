number = int(input())

def sign(n):
    if n == 0:
        print(f"The number {n} is zero.")
    elif n > 0:
        print(f"The number {n} is positive.")
    elif n < 0:
        print(f"The number {n} is negative.")


sign(number)
