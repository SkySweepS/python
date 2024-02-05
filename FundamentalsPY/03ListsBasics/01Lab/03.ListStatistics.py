n = int(input())
l_pos = []
l_neg = []
for i in range(n):
    n1 = int(input())
    if n1 > 0:
        l_pos.append(n1)
    else:
        l_neg.append(n1)

print(l_pos)
print(l_neg)
print(f"Count of positives: {len(l_pos)}")
sum = 0
for i in l_neg:
    sum += i
print(f"Sum of negatives: {sum}")
