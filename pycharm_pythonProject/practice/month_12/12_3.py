import csv
from pathlib import Path
from texttable import Texttable


class UsersManager:
    def __int__(self, list_users: list[list]):
        self.list_users = list_users
        pass

    def register_users(self, account, password):
        for i in self.list_users:
            if i[0] == account:
                return f"该账号已存在！"
        self.list_users.append([account, password, 0])
        self.save_users()
        return f"注册成功！"
        pass

    def login_users(self, account, password):
        for i in self.list_users:
            if i[0] == account and i[1] == password:
                i[2] += 1
                self.save_users()
                return f"登录成功！"
            else:
                return f"账号或密码不匹配！"
        pass

    def show_users(self):

        pass

    @staticmethod
    def get_users():
        list_users = []
        get_path_users = Path(r"..\homework\users.csv")
        with open(get_path_users, "r", encoding="utf-8") as f:
            for row in csv.reader(f):
                list_users.append(row)
        return list_users
        pass

    def save_users(self):
        get_path_users = Path(r"..\homework\users.csv")
        with open(get_path_users, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.list_users)
        return f"success"
        pass


user = UsersManager()

# list_users = []
# get_path_users = Path(r"..\homework\users.csv")
# with open(get_path_users, "r", encoding="utf-8") as f:
#     # while True:
#     #     line = f.readline().rstrip()
#     #     if not line:
#     #         break
#     #     list_users.append([line])
#     for row in csv.reader(f):
#         list_users.append(row)
# print(list_users)

# with open(get_path_users, 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(list_users)

while True:
    print()
    choose = input("").strip()
    if choose == "1":
        register_account = input("").strip()
        register_password = input("").strip()
        register_inf = user.register_users()
        print(register_inf)
        pass
    elif choose == "2":
        login_account = input("").strip()
        login_password = input("").strip()

        pass
    elif choose == "3":

        pass
    else:
        print("error")
        pass
