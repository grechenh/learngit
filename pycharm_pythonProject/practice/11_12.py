a,b,c=list(map(int,input().split()))
x = a+b+c
t_x = type(x)
print(f"{x},{t_x}")

# leecode 11. 盛最多水的容器
height = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(height) - 1
max_sqre = 0
while left <right:
    sqre =( right - left )*min(height[left],height[right])
    max_sqre = max(sqre, max_sqre)
    if height[left] < height[right]:
        left += 1
    else:
        right -=1
print(f"{max_sqre}")
