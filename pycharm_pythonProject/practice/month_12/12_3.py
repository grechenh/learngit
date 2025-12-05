import csv
from pathlib import Path
from texttable import Texttable


class UsersManager:
    def __init__(self, list_users: list[list] = None):
        if list_users is None:
            self.list_users = self.get_users()
        else:
            self.list_users = list_users
        pass

    def register_users(self, account, password):
        for i in self.list_users:
            if i[0] == account:
                return f"该账号已存在！"
                # raise ValueError("该账号已存在！")
        self.list_users.append([account, password, 0])
        self.save_users()
        return f"注册成功！"
        pass

    def login_users(self, account, password):
        for i in self.list_users:
            # print(type(i[0]), type(i[1]),type(password),account,i[0], i[0] == account, i[1] == password)
            if i[0] == account and i[1] == password:
                num = int(i[2])
                num += 1
                i[2] = num
                self.save_users()
                return f"登录成功！"
        return f"账号或密码不匹配！"
        # raise ValueError("账号或密码不匹配!")
        pass

    def show_users(self):
        table = Texttable()
        table.set_cols_align(["c", "c", "c"])
        table.add_rows([["账号", "密码", "登录次数"]] + self.list_users)
        return table.draw()
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
        get_path_users.parent.mkdir(parents=True, exist_ok=True)
        with open(get_path_users, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.list_users)
        return f"save success"
        pass


if __name__ == "__main__":
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
        print("\n***************************************")
        print("1.注册\t2.登录\t3.查看用户信息\t4.退出")
        choose = input("请选择：").strip()
        if choose == "1":
            register_account = input("请输入用户名：").strip()
            register_password = input("请输入密码：").strip()
            register_inf = user.register_users(account=register_account, password=register_password)
            print(register_inf)
            pass
        elif choose == "2":
            login_account = input("请输入用户名：").strip()
            login_password = input("请输入密码：").strip()
            login_inf = user.login_users(account=login_account, password=login_password)
            print(login_inf)
            pass
        elif choose == "3":
            show_users = user.show_users()
            print(show_users)
            pass
        elif choose == "4":
            end = user.save_users()
            print(end)
            exit()
        else:
            print("error")
            pass
