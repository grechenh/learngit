# s = [1, 2, 3, 4, 5, 6]
# s2 = ["q", "w", "e", "r", "t"]
# # s3 = [(s[i], s2[i]) for i in range(min(len(s2),len(s)))]
# s3 = [0]*len(s)
# print(s3)

# s = [1,2]
# s1 = [3,4]
# print(id(s))
# s1[:] = s
# print(id(s1))


# leecode:34. 在排序数组中查找元素的第一个和最后一个位置

nums = [5, 7, 7, 9, 10, 12, 12, 12, 12, 12, 23, 54, 65]
target = 12


def lower_bounds(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


first = lower_bounds(nums, target)
if first == len(nums) or nums[first] != target:
    print([-1, -1])
end = lower_bounds(nums, target + 1) - 1
print([first, end])


