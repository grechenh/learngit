# num1 = int(input("请输入第一个数字:").strip())
# num2 = int(input("请输入第二个数字:").strip())
# print(f"和:{num1:.02f} + {num2:.02f} = {num1+num2:.02f}")
# print(f"差:{num1:.02f} - {num2:.02f} = {num1-num2:.02f}")
# print(f"积:{num1:.02f} * {num2:.02f} = {num1*num2:.02f}")
# if num2 == 0:
#     print("error:除数不能为零！")
# else:
#     print(f"商:{num1:.02f} ÷ {num2:.02f} = {num1/num2:.02f}")
#
#
# get_str = input("请输入一个字符串:").strip()
# for i in range(len(get_str)):
#     num = 0
#     for j in get_str:
#         if get_str[i] == j:
#             num +=1
#     print(f"{get_str[i]}:{num}")
#
#
# dict = {}
# for i in get_str:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# for i in dict.keys():
#     print(f"{i}:{dict[i]}")
#
# num = int(input("请输入一个整数:").strip())
# a = [0]*(num+1)
# if num == 1:
#     print(f"1 到 {num} 的序列: 1", end=" ")
#     print(f"\n{num} 到 1 的序列: 1", end=" ")
#     print(f"\n1 到 {num} 的奇数: 1", end=" ")
#     print(f"\n1 到 {num} 的偶数: 无", end=" ")
# else:
#     for i in range(num):
#         a[i] = 1 + i
#     print(f"1 到 {num} 的序列:",end=" ")
#     for i in range(num):
#         print(a[i], end=" ")
#     print(f"\n{num} 到 1 的序列:",end=" ")
#     for i in range(num):
#         print(a[-1-i], end=" ")
#     print(f"\n1 到 {num} 的奇数:",end=" ")
#     for i in range(0,num,2):
#         print(a[i], end=" ")
#     print(f"\n1 到 {num} 的偶数:",end=" ")
#     for i in range(0,num,2):
#         print(a[i+1], end=" ")
#
# num = int(input("输入学生的分数（0-100）").strip())
# print(f"分数: {num}")
# if 90 <= num <= 100:
#     print("优秀")
# elif 80 <= num < 90:
#     print("良好")
# elif 70 <= num < 80:
#     print("中等")
# elif 60 <= num < 70:
#     print("及格")
# elif 0 <= num < 60:
#     print("不及格")
# else:
#     print("error：输入分数不正确！")
#
# name = input("请输入姓名:")
# age = input("请输入年龄:")
# height = float(input("请输入身高(米):"))
# weight = float(input("请输入体重(公斤):"))
# BMI = weight/height**2
# print(f"姓名:{name}")
# print(f"年龄:{age}")
# print(f"身高:{height:.02f}")
# print(f"体重:{weight:.02f}")
# print(f"BMI 指数:{BMI:.02f}")


