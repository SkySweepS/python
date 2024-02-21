text = input()

text_word = ""

total = text

if text[-1].isdigit():
    new = float(total) // 1
    if float(total) - new == 0:
        total = int(text) + 1
        print(total)
    else:
        total = float(total) + 1
        print(total)







else:
    for i in range(1, len(text) + 1):
        text_word += text[-i]
    print(text_word)

