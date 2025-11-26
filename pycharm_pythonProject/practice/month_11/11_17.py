# start = 3
# n = 4
# nums = [0] * n
# end = start
# for i in range(n):
#     nums[i] = start + 2 * i
# print(nums)
# for i in nums[1:]:
#     print(i)
#     end = end ^ i
# print(end)


# x = ["a", "b", "c", "d", "e"]
# y = ("a", "b", "c", "d", "e")
# z = "abcde"
#
# from random import randint
# r = randint(0, 1)
# if r == 0:
#     x0 = x[2:4]
# else:
#     x0 = y[2:4]
# del r
# if isinstance(x0,tuple):
#     print(x0 + y)
# else:
#     print(x0 + x)


# # 1:正金字塔
# 编写一个程序，实现以下功能：
# •	输入一个整数n（1-9）
# •	使用嵌套循环生成数字金字塔
# •	每行数字从1开始递增
# 示例运行：
# 请输入金字塔层数(1-9): 4
#    1
#   121
#  12321
# 1234321
# a = int(input("请输入金字塔层数(1-9):").strip())
# for i in range(1, a + 1):
#     j = 1
#     print(" " * (a - i), end="")
#     while j <= i:
#         print(j, end="")
#         j += 1
#     j = i
#     while j != 1:
#         j -= 1
#         print(j, end="")
#     print()

# # 题目2：简单计算器
# # 编写一个程序，实现以下功能：
# # •	输入两个数字和一个运算符（+、-、*、/）
# # •	根据运算符执行相应的算术运算
# # •	输出运算结果
# # •	处理除零错误和无效运算符
# # 示例运行：
# # 请输入第一个数字: 15
# # 请输入运算符(+, -, *, /): *
# # 请输入第二个数字: 4
# 15.0 * 4.0 = 60.0
# num1 = int(input("请输入第一个数字:").strip())
# symbol = input("请输入运算符(+, -, *, /):").split()
# num2 = int(input("请输入第二个数字: ").strip())
# if "+" in symbol:
#     print(num1 + num2,end="")
# elif "-" in symbol:
#     print(num1 - num2)
# elif "*" in symbol:
#     print(num1 * num2)
# elif "/" in symbol:
#     if num2 == 0:
#         print("error:被除数不能为零！")
#     else:
#         print(num1 / num2)
# else:
#     print("error:未能识别运算符！")

# # 题目3：字符串反转和统计
# # 编写一个程序，实现以下功能：
# # •	输入一个字符串
# # •	将字符串反转输出（如果用两种或以上方法实现，每多一种实现方法可加10分）
# # •	统计字符串中的字母、数字和其他字符的数量
# # 示例运行：
# # 请输入一个字符串: Hello123!
# # 原始字符串: Hello123!
# # 反转字符串: !321olleH
# # 字母数量: 5
# # 数字数量: 3
# # 其他字符数量: 1
# string = input("请输入一个字符串:")
# # 1：切片
# print(f"反转字符串:{string[::-1]}")
# # 2：字符串循环相加
# down_string = ""
# for i in range(len(string)):
#     down_string += string[-1 - i]
# print(f"反转字符串:{down_string}")
# # 3：reversed()函数调用
# down_string = "".join(list(reversed(string)))
# print(f"反转字符串:{down_string}")
# sum_num = 0
# sum_str = 0
# sum_other = 0
# for i in range(len(string)):
#     if string[i].isalpha():
#         sum_str += 1
#     elif string[i].isdigit():
#         sum_num += 1
#     else:
#         sum_other += 1
# print(f"字母数量:{sum_str}")
# print(f"数字数量:{sum_num}")
# print(f"其他字符数量: {sum_other}")


# # 题目4：九九乘法表生成器（25分）
# # 编写一个程序，实现以下功能：
# # •	使用嵌套循环实现
# # •	格式化输出乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         if i > 1:
#             print(f"{j}x{i}={i * j},", end=" ")
#             i -= 1
#         else:
#             print(f"{j}x{i}={i*j}")
#             break
#     print()


# # 题目5：完美数查找
# # 1.暴力穷举
# n = 10000
# for i in range(1, n + 1):
#     get_sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             get_sum += j
#     if get_sum == i:
#         print(f"{get_sum}")
#
# 2.欧几里得-欧拉定理
# n = 10000
# for i in range(1, n+1):
#     form = 2 ** (i - 1) * (2 ** i - 1)
#     get_sum = 0
#     if form > n:
#         break
#     else:
#         for j in range(1, form):
#             if form % j == 0:
#                 get_sum += j
#         if get_sum == form:
#             print(f"{get_sum}")


