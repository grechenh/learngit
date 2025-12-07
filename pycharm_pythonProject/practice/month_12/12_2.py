# import os
# from pathlib import Path
# get_cwd = Path.cwd()
# get_file = [str(item) for item in get_cwd.iterdir() if item.is_file()]
# # for item in get_cwd.iterdir():
# #     print(item)
# print(get_file)


import os
from pathlib import Path


def fun(path):
    cont = []
    get_path = Path(path)
    if not get_path.exists():
        print("不存在文件")
        return []
    for i in get_path.iterdir():
        if i.is_file() and i.suffix.lower() == ".txt":
            name = os.path.basename(i)
            size = os.path.getsize(i)
            with open(f"{i}", "r+", encoding="utf-8") as f:
                x = f.read()
            len_num = len(x.split("\n"))
            words = [word for word in x.split() if word]
            word_num = len(words)
            char_num = len(x)
            cont.append([name, size, len_num, word_num, char_num])
    return cont


def main():
    get_path = input("路径：")
    if not get_path:
        print("请输入有效的目录路径")
        return
    ans = fun(get_path)
    # C:\Users\chen jia hui\OneDrive\桌面\新建文件夹
    if not ans:
        print("未读取到文件！")
        return
    else:
        with open("fun.csv", "a", encoding="utf-8") as f:
            for item in ans:
                name, size, lines, words, chars = item
                f.write(f"{name},{size},{lines},{words},{chars}\n")

if __name__ == '__main__':
    main()


# from pathlib import Path
# from datetime import datetime
#
#
# def find_path(path, path_list: list):
#     try:
#         get_path = Path(path)
#         for item in get_path.iterdir():
#             if item.is_file() and not item.name.startswith("."):
#                 try:
#                     abs_path = str(item.absolute())
#                     file_size = item.stat().st_size
#                     mod_time = datetime.fromtimestamp(item.stat().st_mtime)
#                     mod_time_str = mod_time.strftime("%Y-%m-%d %H:%M:%S")
#                     path_list.append((abs_path, file_size, mod_time_str))
#                 except (PermissionError, OSError):
#                     pass
#             elif item.is_dir():
#                find_path(str(item), path_list)
#     except (PermissionError, OSError):
#         pass
#
#
# def main():
#     get_list = []
#     in_path = input("路径：").strip()
#     path = Path(in_path)
#     if not path.exists():
#         print("不存在！")
#         return
#     if not path.is_dir():
#         print("不是目录！")
#         return
#     find_path(path, get_list)
#     print(get_list)
#     get_list.sort(key=lambda x: x[0])
#     for file_info in get_list:
#         abs_path, file_size, mod_time = file_info
#         print(f"{abs_path},{file_size},{mod_time}")
#
#
# if __name__ == '__main__':
#     main()
