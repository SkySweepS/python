n = int(input())
list_1 = []
even_list = []
odd_list = []
positive_list = []
negative_list = []
for i in range(n):
    list_1.append(int(input()))

for i1 in range(len(list_1)):
    number = list_1[i1]
    if number % 2 == 0:
        even_list.append(number)
    if number % 2 == 1:
        odd_list.append(number)
    if number < 0:
        negative_list.append(number)
    if number >= 0:
        positive_list.append(number)
where = input()
if where == "even":
    print(even_list)
elif where == "odd":
    print(odd_list)
elif where == "negative":
    print(negative_list)
elif where == "positive":
    print(positive_list)
