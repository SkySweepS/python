n = int(input())
result = 0
word_result = []
count = 0
word_count = 0
for i in range(n):

    word = input()
    if word[-1].isdigit():
        if word_count != 0:
            print("-".join(word_result))
        word_result = []
        count += 1
        word_count = 0
    else:
        if count != 0:
            print(result)
        word_result.append(word)
        count = 0
        result = 0
        word_count += 1

    if count > 0:
        result += int(word)

if word_result == []:
    print(result)
else:
    print("-".join(word_result))

