n = input().split(", ")

def is_palindrome(num):
    reversed_num = num[::-1]
    is_palindrome = True
    if num != reversed_num:
        is_palindrome = False

    return is_palindrome

for i in n:
    print(is_palindrome(i))
