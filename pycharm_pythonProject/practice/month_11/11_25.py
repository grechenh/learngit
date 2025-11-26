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
# for i in sentence:
#     word_count[i] = word_count.get(sentence,0) + 1
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
    if records in student_cnt:
        print("已有该成员！")
        return False
    student_private = dict()
    student_private["name"] = name
    student_private["score"] = score
    student_cnt[records] = student_private
    return True


def get_statistics(records):
    if not records:
        return [0, 0, 0]
    max_score = 0
    min_score = 100
    sum_score = 0
    for i in records.values():
        max_score = max(max_score, i["score"])
        min_score = min(min_score, i["score"])
        sum_score += i["score"]
    avg_score = sum_score / len(records)
    return [max_score, min_score, avg_score]


def find_students_by_score(records, min_score, max_score):
    for i, j in records.items():
        if max_score >= j["score"] >= min_score:
            print(f"学号：{i}  姓名：{j['name']}  分数：{j['score']}\n")


student_cnt = dict()
while True:
    choose = input("1. 添加学生 2. 查看统计 3. 查找学生 4. 退出\n请选择:").strip()
    if choose == "1":
        add_name = input("请输入姓名:")
        try:
            add_records = int(input("请输入学号: "))
            add_score = float(input("请输入分数: "))
            add_student(records=add_records, name=add_name, score=add_score)
            print("添加成功!\n")
        except:
            print("输入必须为数字！")
    elif choose == "2":
        ans = get_statistics(records=student_cnt)
        print(f"最高分为：{ans[0]}\n最低分为：{ans[1]}\n平均分为:{ans[2]:.02f}\n")
    elif choose == "3":
        get_max = int(input("请输入要查询范围的最高分：").strip())
        get_min = int(input("请输入要查询范围的最低分：").strip())
        print(f"{get_min} - {get_max} 的学生信息为：")
        find_students_by_score(records=student_cnt, min_score=get_min, max_score=get_max)
    elif choose == "4":
        exit()
    else:
        print("error")
