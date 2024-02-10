word_input = input()

vowel = "a o u e i A O U E I".split(" ")
new = [i for i in word_input if not i in vowel]
print("".join(new))