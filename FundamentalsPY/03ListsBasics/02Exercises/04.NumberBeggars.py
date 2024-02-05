nums = input().split(", ")
beggers = int(input())
nums_list = []
beggers_list = [0] * beggers
for i in nums:
    nums_list.append(int(i))

for i1 in range(len(nums_list)):

    index = i1 % beggers
    beggers_list[index] += nums_list[i1]

print(beggers_list)