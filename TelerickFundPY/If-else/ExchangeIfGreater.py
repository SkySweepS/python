Pastebin
API
tools
faq
paste
Login
Sign
up
Advertisement
SHARE
TWEET
svephoto
Everest[Python]
svephoto
Jul
21
st, 2021(edited)
3, 255
0
Never
Add
comment
Not
a
member
of
Pastebin
yet? Sign
Up, it
unlocks
many
cool
features!
0.80
KB | None |

command = input()
initial_hiking_meters = 5364
the_peak_height = 8848
days_for_hiking = 1

while command != "END":
    meters_to_hike = int(input())

    if command == "Yes":
        days_for_hiking += 1
        if days_for_hiking > 5:
            print("Failed!")
            print(f"{initial_hiking_meters}")
            break
        initial_hiking_meters += meters_to_hike
    else:
        initial_hiking_meters += meters_to_hike
    if initial_hiking_meters >= the_peak_height:
        print(f"Goal reached for {days_for_hiking} days!")
        break

    command = input()

if command == "END":
    if initial_hiking_meters >= the_peak_height:
        print(f"Goal reached for {days_for_hiking} days!")
    else:
        print("Failed!")
        print(f"{initial_hiking_meters}")

Advertisement
Add
Comment
Please, Sign
In
to
add
comment
Advertisement
Public
Pastes

Reti
endgame
Python | 39
min
ago | 4.01
KB
Sol
C + + | 41
min
ago | 1.28
KB
numbers
Python | 46
min
ago | 0.79
KB
G2A.com
Free
Gift
Card
Guide
Feb
2024
GetText | 51
min
ago | 0.30
KB
ding
JSON | 58
min
ago | 0.00
KB
W2L1(Lecture3) - FP24 - Vlad - Batch2Q5 - WL
Haskell | 1
hour
ago | 0.44
KB
computer
store
Python | 1
hour
ago | 0.60
KB
createBinarySearchTree.c
C | 1
hour
ago | 3.20
KB

Advertisement
create
new
paste / syntax
languages / archive / faq / tools / night
mode / api / scraping
api / news / pro
privacy
statement / cookies
policy / terms
of
service / security
disclosure / dmca / report
abuse / contact

By
using
Pastebin.com
you
agree
to
our
cookies
policy
to
enhance
your
experience.
Site
design & logo © 2024
Pastebin
We
use
cookies
for various purposes including analytics.By continuing to use Pastebin, you agree to our use of cookies as described in the Cookies Policy.OK, I Understand
Not
a
member
of
Pastebin
yet?
Sign
Up, it
unlocks
many
cool
features!

