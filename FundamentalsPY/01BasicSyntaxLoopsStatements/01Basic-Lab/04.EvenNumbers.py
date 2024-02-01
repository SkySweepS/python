n = int(input())
count = 0
while True:
    i = int(input())
    if i % 2 == 1:
        print(f"{i} is odd!")
        break
    if count == (n - 1) and i % 2 == 0:
        print("All numbers are even.")
        break
    count += 1

