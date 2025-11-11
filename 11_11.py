# get_list = [x for x in range(1, 31)]
# out_list = []
# i = 0
# while len(get_list) >= 15:
#     i = (i + 8) % len(get_list)
#     del_people = get_list.pop(i)
#     out_list.append(del_people)
# print(f"{out_list=}")


# n = int(input().replace(" ",""))
# if n%2 == 0:
#     f = ((n**2 + 10)*12 - 5)/3.0
# else:
#     f = ((n**3 + 10)*21 + 5)/7.0
# if f >10:
#     print(f"{f:.4f}")
# else:
#     print("error")


# get_num = input().split()
# if int(get_num[0]) >= int(get_num[1])*3:
#     f = ((int(get_num[0]) ** 2 + 10) * 12 - 5) / 3.0 + ((int(get_num[1])**3 + 10)*21 + 5)/7.0
# else:
#     f = ((int(get_num[0]) ** 3 + 10) * 21 + 5) / 7.0 + ((int(get_num[1]) ** 2 + 10) * 12 - 5) / 3.0
# if f > 10:
#     print(f"{f:.4f}")
# else:
#     print("error")

#
# n1 = input().split()
# n2 = input().split()
# de = ((int(n1[0]) - int(n2[0])) ** 2 + (int(n1[1]) - int(n2[1])) ** 2) ** (1 / 2)
# dm = abs(int(n1[0]) - int(n2[0])) + abs(int(n1[1]) - int(n2[1]))
# change = abs(dm - de)
# print(f"{de},{dm}")
# print(f"{change}")




# leecode:15.三数之和
nums = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
nums.sort()
num = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    j = i + 1
    k = len(nums) - 1
    print(f"{i=},{j},{k}")
    while j < k:
        if int(nums[i]) + int(nums[j]) + int(nums[k]) < 0:
            j += 1
            print(f"{j},{i}")
        elif int(nums[i]) + int(nums[j]) + int(nums[k]) > 0:
            k -= 1
            print(f"{k=},{i}")
        else:
            num.append([nums[i], nums[j], nums[k]])
            j += 1
            while j<k and nums[j] == nums[j - 1]:
                print(f"{nums[j]=},{nums[j-1]=},{j=},{k=}")
                j += 1
            k -= 1
            while j<k and nums[k] == nums[k + 1]:
                print(f"{nums[k]=}")
                k -= 1
print(f"{num}")


