from pathlib import Path
import os
from datetime import datetime

def lookup_path(path: str):
    path_all = []

    directory = Path(path)

    for item in directory.iterdir():
        if item.is_file():
            path_all.append(str(item))
        elif item.is_dir():
            path_all.extend(lookup_path(str(item)))
    return path_all

p = input("璇疯緭鍏ョ數鑴戜腑鐨勬枃浠跺す璺緞锛�").strip()
# p = r'D:\jyd涓婅璧勬枡'

# sorted(lookup_path(p), key=lambda x: os.path.basename(x))

for item in sorted(lookup_path(p)):

    if not os.path.basename(item).endswith('.txt'):
        continue

    if os.path.exists(item):
        pass
    else:
        print(item, "鏂囦欢涓嶅瓨鍦�")
        continue

    # 妫€鏌ユ枃浠舵槸鍚﹀彲璇�
    readable = os.access(item, os.R_OK)
    if not readable:
        print(item, "鏂囦欢涓嶆槸鍙鏂囦欢")
        continue

    # 妫€鏌ユ枃浠舵槸鍚﹀彲鍐�
    # writable = os.access(item, os.W_OK)
    # if not writable:
    #     print(item, "鏂囦欢涓嶆槸鍙啓鏂囦欢")

    # 妫€鏌ユ枃浠舵槸鍚﹀彲鎵ц锛堝湪鏌愪簺骞冲彴涓婏紝杩欏彲鑳戒笉閫傜敤锛�
    # executable = os.access(item, os.X_OK)
    # if not executable:
    #     print(item, "鏂囦欢涓嶆槸鍙墽琛屾枃浠�")

    # print(f'Readable: {readable}, Writable: {writable}, Executable: {executable}')

    """
    try:
        with open(item, 'r') as file:
            pass
    except IOError:
        print(item, "鏂囦欢涓嶆槸鍙鏂囦欢")

    try:
        with open(item, 'r+') as file:
            pass
    except IOError:
        print(item, "鏂囦欢涓嶆槸鍙啓鏂囦欢")
    """
    size = os.path.getsize(item)
    # timestamp = os.path.getmtime(item)
    # mtime = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    # print(f"{item}, 瀛楄妭澶у皬锛歿size}, 淇敼鏃堕棿锛歿mtime}")
    with open(item, 'r', encoding='utf-8') as file:
        content = file.read()
        content_lines = content.count('\n') + 1
        content_char_number = len(content)
        content_words = len(content.split())
    # print(f"{os.path.basename(item)} {size} {content_lines} {content_words} {content_char_number}")
        with open("results.csv", 'a+', encoding='utf-8') as file:
            file.write(f"{os.path.basename(item)}\t{size}\t{content_lines}\t{content_words}\t{content_char_number}\n")


# directory = Path(p)
# for item in directory.iterdir():
#     print(item)