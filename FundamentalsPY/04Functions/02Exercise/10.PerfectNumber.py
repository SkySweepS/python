n = int(input())


def sum_num(n):
    nums = []

    for i in range(1, n):
        if n % i == 0:
            nums.append(int(i))

    num = sum(nums)
    return num


if sum_num(n) == n:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
