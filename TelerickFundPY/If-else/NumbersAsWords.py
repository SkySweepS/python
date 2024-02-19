number = int(input())
if number == 0:
    print("zero")


hundreds = number // 100
tens = (number - hundreds * 100) // 10
ones = number - hundreds * 100 - tens * 10


hundred_string = ""
ten_string = ""
one_string = ""
and_string = ""
last_string = ""
if ones != 0:
    if ones == 1:
        one_string += "one"
    elif ones == 2:
        one_string += "two"
    elif ones == 3:
        one_string += "three"
    elif ones == 4:
        one_string += "four"
    elif ones == 5:
        one_string += "five"
    elif ones == 6:
        one_string += "six"
    elif ones == 7:
        one_string += "seven"
    elif ones == 8:
        one_string += "eight"
    elif ones == 9:
        one_string += "nine"
if tens == 0:
    pass
elif tens == 1 and ones != 0:
    if ones == 1:
        ten_string = "eleven"
        one_string = ""
    elif ones == 2:
        ten_string = "twelve"
        one_string = ""
    elif ones == 3:
        ten_string = "thirteen"
        one_string = ""
    elif ones == 7:
        ten_string = "seventeen"
        one_string = ""
    elif ones == 9:
        ten_string = "nineteen"
        one_string = ""
else:
    if tens == 1:
        ten_string += "ten "
    elif tens == 2:
        ten_string += "twenty "
    elif tens == 3:
        ten_string += "thirty "
    elif tens == 4:
        ten_string += "forty "
    elif tens == 5:
        ten_string += "fifty "
    elif tens == 6:
        ten_string += "sixty "
    elif tens == 7:
        ten_string += "seventy "
    elif tens == 8:
        ten_string += "eighty "
    elif tens == 9:
        ten_string += "ninety "

if hundreds > 0:
    if hundreds == 1:
        hundred_string += "one hundred"
    elif hundreds == 2:
        hundred_string += "two hundred"
    elif hundreds == 3:
        hundred_string += "three hundred"
    elif hundreds == 4:
        hundred_string += "four hundred"
    elif hundreds == 5:
        hundred_string += "five hundred"
    elif hundreds == 6:
        hundred_string += "six hundred"
    elif hundreds == 7:
        hundred_string += "seven hundred"
    elif hundreds == 8:
        hundred_string += "eight hundred"
    elif hundreds == 9:
        hundred_string += "nine hundred"



if hundreds > 0 and (tens > 0 or ones > 0):
    and_string += " and "



last_string = hundred_string + and_string + ten_string + one_string
print(last_string)
