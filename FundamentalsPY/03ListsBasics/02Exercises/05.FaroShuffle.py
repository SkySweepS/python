deck = input().split(" ")
shuffels = int(input())
slice = len(deck) // 2
deck_1 = [""] * slice
deck_2 = [""] * slice
final_deck = [""] * len(deck)
for i in range(shuffels):


    for i in range(len(deck)):

        if i < slice:
            deck_2[i] = deck[i + slice]

    for i in range(len(deck_1)):
        deck_1[i] = deck[i]

    for i in range(len(final_deck)):
        if i % 2 == 0:
            final_deck[i] = deck_1[int(i / 2)]
        else:
            final_deck[i] = deck_2[int(i / 2)]
    for i in range(len(deck)):
        deck[i] = final_deck[i]

print(final_deck)
