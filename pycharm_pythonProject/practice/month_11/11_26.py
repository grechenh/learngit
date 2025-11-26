# b = [4,5,6]
# def p1():
#     a =[1,2,3]
#     c =b[1:2]
#     return a,c
#
# def p2():
#     return "world"

# def x():
#     a =p1()
#     b =p2()
#     return a + b


# inventory = {'apple': (2.5, 10), 'banana': (1.8, 15), 'orange': (3.0, 8)}
# all_price = dict()
# sort_dict =[]
# for i ,(price , num)in inventory.items():
#     all_price[i] = price * num
# min_num = min(inventory.items(), key=lambda x: x[1][1])[0]
# print(f"各商品总价值:{all_price} \n库存最少的商品:{min_num}")
# print("按名称排序的商品信息:")
# sorted_dict = sorted(inventory.keys())
# for i in sorted_dict:
#     price = inventory[i][0]
#     num = inventory[i][1]
#     print(f"*{i} - 价格: {price}, 数量: {num}, 总价值: {all_price[i]}*")


# def validate_numbers(func):
#     def inner(a, b):
#         if not isinstance(a, (int, float)) and not isinstance(b, (int, float)):
#             raise TypeError("错误输入: 参数必须是数字!")
#         return func(a, b)
#     return inner
#
#
# def create_math_operation(operation):
#     @validate_numbers
#     def math_operation(a, b):
#         """'add', 'subtract', 'multiply', 'divide'"""
#         if operation == "add":
#             return a + b
#         elif operation == "subtract":
#             return a - b
#         elif operation == "multiply":
#             return a * b
#         elif operation == "divide":
#             if b == 0:
#                 raise TypeError("错误输入: 除数不能为零！")
#             else:
#                 return a / b
#         else:
#             raise ValueError(f"不支持的操作: {operation}")
#     return math_operation
#
#
# get_add = create_math_operation("add")
# print(get_add(3, 5))