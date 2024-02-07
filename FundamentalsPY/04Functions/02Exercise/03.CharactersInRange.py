char1 = input()
char2 = input()

def char_range(c1, c2):
    chars = []
    for i in range(ord(c1) + 1, ord(c2)):
        chars.append(chr(i))
    return " ".join(chars)

print(char_range(char1, char2))
