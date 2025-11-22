# leecode：209长度最小数组
# nums = [1, 2, 4, 7, 9, 4, 2, 4, 7, 1, 2, 4]
# target = 7
# left = 0
# s = 0
# end = len(nums) + 1
# for right, num in enumerate(nums):
#     s += num
#     while s >= target:
#         end = min(end, right - left + 1)
#         s -= nums[left]
#         left += 1
#         print(f"{left},{right}")
# if end > len(nums):
#     print("0")
# else:
#     print(f"{end}")


# leecode：713乘积小于k的子数组
nums = [3,4,63,4,23,54,23,]
k = 46
left = 0
sum = 1
end = 0
if k <= 1:
    print(0)
for right, num in enumerate(nums):
    sum *= num
    while sum >= k:
        sum /= nums[left]
        left += 1
    end += right - left + 1
print(end)
