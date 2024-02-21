n = input()
num = 0
if n.isdigit():
    num = int(n)
else:
    if n == "J":
        num = 11
    elif n == "Q":
        num = 12
    elif n == "K":
        num = 13
    elif n == "A":
        num = 14

for i in range(2, 11):
    print(i, "of spades,", i, "of clubs,", i, "of hearts,", i, "of diamonds")
    if i == num:
        break

if n == "J" or num >= 11:
    j = "J"
    print(j, "of spades,", j, "of clubs,", j, "of hearts,", j, "of diamonds")

if n == "Q" or num >= 12:
    q = "Q"
    print(q, "of spades,", q, "of clubs,", q, "of hearts,", q, "of diamonds")


if n == "K" or num >= 13:
    k = "K"
    print(k, "of spades,", k, "of clubs,", k, "of hearts,", k, "of diamonds")

if n == "A" and num == 14:
    a = "A"
    print(a, "of spades,", a, "of clubs,", a, "of hearts,", a, "of diamonds")





