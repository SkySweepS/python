n = input().split(" ")
count = 0
num = 0
for i in range(len(n)):
    if i % 2 == 0:
        if n[i] > n[i +1 <= len(n)]:
            num += 1
            print("yes")
        else:
            count += 1
            print("no")
        
    if i % 2 == 1:
        if n[i] < n[i +1 <= len(n)]:
            num += 1 
            print("yes")
        else:
            count += 1
            print("no")

