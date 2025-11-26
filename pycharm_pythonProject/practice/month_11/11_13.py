# 42. 接雨水
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
left = [0]*len(height)
right = [0]*len(height)
list_sum = []
get_sum = 0
# left.append(height[0])
# right.append(height[-1])
for i in range(len(height)):
    if i == 0:
        left[i] = height[0]
        right[i] = height[-1]
    else:
        left[i] = max(height[i], left[i - 1])
        right[i] = max(height[-1 - i], right[i -1])
        # print(f"{left}{right}")
for i in range(len(height)):
    list_sum.append(min(left[i], right[-i-1]))
# print(f"{list_sum},{left},{right}")
for i in range(len(height)):
    get_sum += (list_sum[i] - height[i])
print(f"{get_sum}")


