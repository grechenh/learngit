# string = input("输入字符串：").lower().title()
# print(string)
#
# numbers = []
# get_num = 0
# while get_num >= 0:
#     get_num = int(input())
#     if get_num >= 0:
#         numbers.append(get_num)
# end = sum(numbers)//len(numbers)
# print(f"{end:.02f}")
#
#
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8]
# sum_list = []
# only_list1 = []
# for i in range(len(list1)):
#     num = 0
#     for j in list2:
#         if j == list1[i]:
#             sum_list.append(j)
#             num += 1
#             break
#     if num == 0:
#         only_list1.append(list1[i])
# print(f"共有的元素: {sum_list}")
# print(f"仅在list1中的元素: {only_list1}")

# from collections import deque
# que:deque[int] = deque()
# # 入队，添加队尾
# que.append(1)
# que.append(2)
# que.append(3)
# # 访问队首
# front:int = que[0]
# # 出队
# pop:int = que.popleft()

