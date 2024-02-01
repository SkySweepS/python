n = int(input())

for i in range(0,n):
    for i1 in range(0,n):
        for i2 in range(0,n):
            print(f"{chr(97 + i)}{chr(97 + i1)}{chr(97 + i2)}")
