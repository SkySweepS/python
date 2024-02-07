password = input()

def new_check(pw):
    if not 6 <= len(pw) <= 10:
        print("Password must be between 6 and 10 characters")
def len_check(pw):
    valid = 0
    if not 6 <= len(pw) <= 10:
        valid += 1
    n = 0
    for i in pw:

        if 47 < ord(i) < 58:
            n += 1
        if not 47 < ord(i) < 58 and not 64 < ord(i) < 91 and not 96 < ord(i) < 123:
            valid += 1
    if n < 2:
        valid += 1
    return valid


def digit_check(pw):
    number = 0

    for i in pw:
        if 47 < ord(i) < 58:
            number += 1

    return number


def simbol_check(pw):
    false = 0
    for i in password:

        if not 47 < ord(i) < 58 and not 64 < ord(i) < 91 and not 96 < ord(i) < 123:
            false += 1

    return false


number = digit_check(password)
false = simbol_check(password)
valid = len_check(password)
new_check(password)
if valid == 0:
    print("Password is valid")
if false != 0:
    print("Password must consist only of letters and digits")
if number < 2:
    print("Password must have at least 2 digits")
