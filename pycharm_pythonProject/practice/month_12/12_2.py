# import os
# from pathlib import Path
# get_cwd = Path.cwd()
# get_file = [str(item) for item in get_cwd.iterdir() if item.is_file()]
# # for item in get_cwd.iterdir():
# #     print(item)
# print(get_file)


# import os
# from pathlib import Path
#
#
# def fun(path):
#     cont = []
#     get_path = Path(path)
#     if not get_path.exists():
#         return f"不存在文件"
#     for i in get_path.iterdir():
#         if i.is_file() and i.suffix.lower() == ".txt":
#             name = os.path.basename(i)
#             size = os.path.getsize(i)
#             with open(f"{i}", "r+", encoding="utf-8") as f:
#                 x = f.read()
#             len_num = len(x.split("\n"))
#             words = [word for word in x.split() if word]
#             word_num = len(words)
#             char_num = len(x)
#             cont.append([name, size, len_num, word_num, char_num])
#     return cont
#
#
# get_path = input("路径：")
# ans = fun(get_path)
# # C:\Users\chen jia hui\OneDrive\桌面\新建文件夹
# with open("fun.csv", "a", encoding="utf-8") as f:
#     for item in ans:
#         name, size, lines, words, chars = item
#         f.write(f"{name},{size},{lines},{words},{chars}\n")


