n = int(input())
word = input()
list = []
for i in range(n):
    string = input()
    list.append(string)
print(list)
for i1 in range(len(list) - 1, -1, -1):
    element = list[i1]
    if word not in element:
        list.remove(element)
print(list)