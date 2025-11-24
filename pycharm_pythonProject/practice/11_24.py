# def f(i , j):
#     # for a in range(i):
#     #     print("***")
#     # print("-"*j)
#     return  "\n".join(["*"*j for _ in range(i)])
# print(f(2,8))


# def f(a:int):
#     return [n for n in range(1,a + 1) if n%2 == 0]
# print(f(500))


# def f(x: list[int], y: list[int], z: list[int]):
#     return [x1 * y1 + z1 if x1 > 100 else y1 + 3 * z1 for x1, y1, z1 in zip(x, y, z)]
#
#
# print(f([101, 11, 22], [222, 33, 44], [11, 55, 66]))

# import random
# nums = [random.randint(1,100) for _ in range(10)]
# min_nums = min(nums)
# max_nums = max(nums)
# avg = sum(nums)/len(nums)
# print(f"{nums}\n{max_nums}\n{min_nums}\n{avg:.02f}")


# original_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# reversed_list1 = original_list[::-1]
# reversed_list2 = list(reversed(original_list))
# reversed_list3 = [original_list[x] for x in range(len(original_list) - 1, -1, -1)]
# print(f"{reversed_list1}\n{reversed_list2}\n{reversed_list3}")


# def f1(x):
#     return [x for x in range(1, x + 1) if x % 3 == 0]
#
#
# def f2(x):
#     return [x for x in range(1, x + 1) if x % 5 == 0]
#
#
# x = 50
# c = []
# for i, j in zip(f1(x), f2(x)):
#     c.append(i + j)
# c += max(f1(x)[len(c):], f2(x)[len(c):])
# print(c)


