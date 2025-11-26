# from random import randint
# state = randint(1,12)
# print(f"{state}")
# match state:
#     case 1|3|5|7|8|10|12:
#         print("31")
#     case 4|6|9|11:
#         print("30")
#     case _:
#         print("?")
# from random import randint
# print(f"{num1}") if (num1:=randint(1,100)) >(num2 :=randint(1,100)) else print(f"{num2}")
# print(f"{num1},{num2}")
# print(f"{max_num}")
#
#
# state = 2
# week = 1
# while week < 10:
#     state = state + state * 2
#     week += 1
#     print(f"{state=},{week=}")



# 编写温度单位转换程序：
# 1. 提示用户输入温度值和单位（C表示摄氏度，F表示华氏度）
# 2. 如果输入的是摄氏度，转换为华氏度：F = C × 9/5 + 32
# 3. 如果输入的是华氏度，转换为摄氏度：C = (F - 32) × 5/9
# 4. 使用if语句判断转换方向
# 5. 输出转换结果，保留1位小数
# 6. 要求处理大小写输入（如'c'和'C'都应该识别）
# temp = input()
# temp_list = temp.strip()
# temp_num = float(temp_list[:-1])
# if temp_list[-1] == "c" or temp_list[-1] =="C":
#     temp_f = temp_num*9/5+32
#     print(f"{temp_f:.2f}F")
# elif temp_list[-1] == "f" or temp_list[-1] =="F":
#     temp_c = (temp_num-32)*5/9
#     print(f"{temp_c:.2f}c")






# 编写用户登录验证程序：
# 1. 预设正确的用户名 "admin" 和密码 "123456"
# 2. 提示用户输入用户名和密码
# 3. 使用if语句验证用户名和密码是否正确
# 4. 如果用户名正确，检查密码是否正确
# 5. 根据验证结果输出相应信息
# 6. 注意字符串比较的大小写问题
#
# 示例：
# 输入：用户名 admin，密码 123456
# 输出：登录成功！
#
# 输入：用户名 admin，密码 wrong
# 输出：密码错误
#
# 输入：用户名 user，密码 123456
# 输出：用户名不存在
# admin_name = "admin"
# admin_pass = 123456
# get_name = input()
# get_pass = input()
# if get_name == admin_name and get_pass == str(admin_pass):
#     print("true")
# elif get_name != admin_name:
#     print(" name error")
# else:
#     print("pass error")




# 编写购物车价格计算程序：
# 1. 提示用户输入商品单价和购买数量
# 2. 计算总价（单价 × 数量）
# 3.使用if语句判断总价是否超过100元，如果超过则打9折。
# 4. 输出原始总价和折后价格（如果打折）
# 5. 要求使用字符串格式化显示金额（保留2位小数）
#
# 示例：
# 输入：单价 25.5，数量 4
# 输出：原始总价：102.00元，折后价格：91.80元

# get_price = input()
# get_num = input()
# get_sum = float(get_num)*int(get_price)
# if get_sum > 100:
#     print(f"{get_sum:.2f}")
#     after_sum = get_sum*0.9
#     print(f"{after_sum:.2f}")
# else:
#     print("error")




#闰年判断器：
# 1. 用户输入年
# 2. 判断同时满足被4整除且不被100整除，或者被400整除，则输出“闰年”，否则输出“平年”

# get_year = int(input())
# if get_year%4==0 and get_year%100!=0 or get_year%400 == 0:
#     print("润")
# else:
#     print("平")



tuple1 = (100, 200, 300, 400, 500)
for i in tuple1:
    print(i)
for i in range(len(tuple1)):
    print(i, tuple1[i])
for i, val in enumerate(tuple1):
    print(i, val)








