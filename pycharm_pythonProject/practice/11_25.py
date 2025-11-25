# def printStar1() :
#     print("*" * 3)
#     def printStar2() :
#         print("*" * 4)
#     return printStar2
# f = 1
# print("鍙橀噺f鎸囧悜int鏁版嵁瀵硅薄绫诲瀷绌洪棿锛� ", f)
# f = printStar1()
# print("鍙橀噺f鎸囧悜鍑芥暟瀵硅薄绫诲瀷绌洪棿锛� ", f)
# f()


# def printStar1() :
#     print("*" * 3)
#     # return 111
#     # return None
# def printStar2() :
#     print("*" * 4)
#     # return 999
# s = []
# s.append(printStar1)
# s.append(printStar2)
# print(s)
# print(s[0])
# print(s[1])
# r_0 = s[0]()
# r_1 = s[-1]()
# print(r_0)
# print(r_1)


# def printstar1():
#     print("*" * 1)
#
#
# def printstar2():
#     print("*" * 2)
#
#
# def printstar3():
#     print("*" * 3)
#
#
# def printstar(a, b):
#     # for _ in range(b):
#     #     a()
#     dict1 = {"printstar1":printstar1(),"printstar2":printstar2(),"printstar3":printstar3()}
#     for _ in range(b):
#         dict1[a]
#
#
# printstar("printstar2", 3)
# print(type(printstar1))


# sentence = list(set(input("输入:").strip().lower().split()))
# sentence.sort()
# print(sentence)

# word_count = dict()
# sentence = list(input("输入: ").strip().split())
# for i in sentence:
#     if i in word_count:
#         word_count[i] += 1
#     else:
#         word_count[i] = 1
# print(word_count)


# from math import inf
# inventory = {'apple': (2.5, 10), 'banana': (1.8, 15), 'orange': (3.0, 8)}
# price = dict()
# min_num = inf
# min_name = ""
# sort_dict =[]
# for i in inventory:
#     price[i] = inventory[i][0] * inventory[i][1]
#     if inventory[i][1] < min_num:
#         min_name = i
#         min_num = inventory[i][1]
# print(f"各商品总价值:{price} \n库存最少的商品:{min_name} {min_num}")
# for i in inventory.keys():
#     sort_dict.append(i)
# print("按名称排序的商品信息:")
# for i in range(len(sort_dict)):
#     print(f"*{sort_dict[i]} - 价格: {inventory[sort_dict[i]][0]}, 数量: {inventory[sort_dict[i]][1]}, 总价值: {price[sort_dict[i]]}*")


# def  process_numbers(numbers:list[int]):
#     max_val = max(numbers)
#     min_val = min(numbers)
#     avg_val = sum(numbers)/len(numbers)
#     even_list = [x for x in numbers if x%2 == 0]
#     return (max_val, min_val, avg_val, even_list)
#
#
# ans = process_numbers([12, 45, 23, 67, 34, 89, 56])
# print(f"最大值: {ans[0]}, 最小值: {ans[1]}, 平均值: {ans[2]:.02f}, 偶数列表: {ans[3]}")


# {学号: {'name': 姓名, 'score': 分数}}
def add_student(records, name, score):
    student_private = dict()
    student_private["name"] = name
    student_private["score"] = score
    student_cnt[records] = student_private
    return student_cnt


# def get_statistics(records):
# #     for i in student_cnt.keys():
#
# def find_students_by_score(records, min_score, max_score) :


student_cnt = dict()
choose =input("1. 添加学生 2. 查看统计 3. 查找学生 4. 退出\n请选择:").strip()
if choose == "1":
    add_records = input("请输入学号: ")
    add_name = input("请输入姓名:")
    add_score = input("请输入分数: ")
    add_student(add_records, add_name, add_score)
    print("添加成功!")
# elif choose == "2":
#
# elif choose == "3":
# elif choose == "4":
# else:
#     print("error")
print(student_cnt)

