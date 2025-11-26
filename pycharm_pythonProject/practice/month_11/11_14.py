import random
# x = [0] * 1000000
# num = random.randint(3, 7)
# print(f"共有{num}人")
# x2 = [0] * num
# get_sum = len(x) // num
# for i in range(get_sum):
#     for i1 in range(len(x2)):
#         get_random = random.randint(0, num - 1)
#         if len(x) - sum(x2) < get_random:
#             x2[i1] = x2[i1] + len(x) - sum(x2)
#         else:
#             x2[i1] = x2[i1] + get_random
# less = x % num
# print(f"{less},{get_sum}")
# out = num - less
# print(f"前{less}个人有：{get_sum + 1}")
# print(f"后{out}个人有：{get_sum}")
# print(f"{x2}")
# print(f"{sum(x2)}")


# x = [0] * 1000000
# num = random.randint(3, 7)
# print(f"共有{num}人")
# x2 = [0] * num
# while sum(x2) != len(x):
#     for i in range(len(x2)):
#         get_random = random.randint(0, num - 1)
#         if len(x) - sum(x2) < get_random:
#             x2[i] += len(x) - sum(x2)
#         else:
#             x2[i] += get_random
# print(f"{x2}")

# 哈希表；两数和
# target = 9
# nums = [0,7,2,1]
# dict1 = {}
# for i, num in enumerate(nums):
#     if target - nums[i] in dict1:
#         print(dict1)
#         print([i+1, dict1[target - nums[i]]+1])
#     else:
#         dict1[num] = i

