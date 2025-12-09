import time
from abc import abstractmethod
from datetime import datetime
import re


class Account:
    def __init__(self, number=None, name=None, balance=0):
        self.accountNumber = number
        self.accountName = name
        self.balance = balance

    def __str__(self):
        return f"账户：{self.accountNumber} 账号名：{self.accountName} 余额：{self.balance}"

    # @abstractmethod
    # def register(self, name):
    #     now = datetime.now()
    #     account_str = re.findall(r"\d+", str(now))
    #     account_num = "".join(account_str)
    #     self.accountNumber = account_num
    #     self.cont[self.accountNumber] = [name, self.balance]

    @abstractmethod
    def deposit(self, money):
        self.balance += money

    @abstractmethod
    def withdrawal(self, lose_money):
        self.balance -= lose_money

    # @abstractmethod
    # def query(self):
    #     pass


class SavingsAccount(Account):
    def __init__(self, number=None, name=None, balance=0, year_interest_rate=0.03):
        super().__init__(number, name, balance)
        self.yearInterestRate = year_interest_rate
        self.type = "储蓄账户"

    def __str__(self):
        return f"账户：{self.accountNumber} 账号名：{self.accountName} 余额：{self.balance} 类型：{self.type}"

    def deposit(self, money):
        super().deposit(money)

    def withdrawal(self, lose_money):
        if self.balance < lose_money:
            return
        super().withdrawal(lose_money)
        return True
    def calculate_interest(self, days):
        self.balance = self.balance *days * self.yearInterestRate/365

class CheckingAccount(Account):
    def __init__(self, number=None, name=None, balance=0, overdraft_limit=500):
        super().__init__(number, name, balance)
        self.overdraftLimit = overdraft_limit
        self.type = "支票账户"

    def __str__(self):
        return f"账户：{self.accountNumber} 账号名：{self.accountName} 余额：{self.balance} 类型：{self.type}"

    def deposit(self, money):
        super().deposit(money)

    def withdrawal(self, lose_money):
        if self.balance + self.overdraftLimit < lose_money:
            return
        super().withdrawal(lose_money)
        return True


class BankCLI:
    def __init__(self):
        self.current_account = None
        self.dict_account = {"20251234567891": CheckingAccount("20251234567891", "cb", 4399)}

    def show(self):
        """显示主菜单"""
        print("\n" + "=" * 50)
        print("🏦 银行账户管理系统")
        print("=" * 50)
        if self.current_account:
            print(f"当前账户: {self.current_account.accountNumber}({self.current_account.accountName}) ")
            print(f"余额: ${self.current_account.balance:.2f}\n")
        print("1.创建账户   2.选择账户    3.存款    4.取款  \n5.查询     6.利息计算（仅储蓄账户）    0.退出 ")

    def run(self):
        while True:
            time.sleep(2)
            self.show()
            try:
                choose = input("\n请输入选项(0-6)：").strip()
                if choose == "1":  # 创建账户
                    self.create_count()
                elif choose == "2":  # 选择账户
                    self.choose_account()
                elif choose == "3":  # 存款
                    self.deposit_account()
                elif choose == "4":  # 取款
                    self.withdrawal()
                elif choose == "5":  # 查询
                    self.check_account()
                elif choose == "6":  # 利息计算（仅储蓄账户）
                    self.calculate_interest()
                # elif choose == "7":  # 透支管理（仅支票账户）
                #     self.view_overdraft()
                elif choose == "0":  # 退出
                    print("exit success")
                    exit()
                else:
                    print("error")
            except KeyboardInterrupt:
                print("\n系统中断！")
                break

    def create_count(self):
        get_type = input("选择储蓄账户或支票账户(1/2):").strip()
        account_name = input("账户名称:").strip()
        account_balance = int(input("账户余额:").strip())
        now = datetime.now()
        account_str = re.findall(r"\d+", str(now))
        account_num = "".join(account_str)
        if get_type == "1":
            account = SavingsAccount(account_num, account_name, account_balance)
        elif get_type == "2":
            account = CheckingAccount(account_num, account_name, account_balance)
        else:
            print("重新选择账户类型！")
        print("创建成功！")
        if not self.current_account:
            """没有登录则登录"""
            self.dict_account[account_num] = account
            self.current_account = account

    def choose_account(self):
        if not self.current_account:
            choose_num = input("请输入账户号：").strip()
            if choose_num not in self.dict_account:
                print("没有该账户，请重新输入！")
            else:
                self.current_account = self.dict_account[choose_num]
        else:
            print("已经登录账户！")

    def deposit_account(self):
        if not self.current_account:
            print("请先创建或选择账户！")
        else:
            try:
                deposit_money = int(input("请输入存款数额：").strip())
                if deposit_money <= 0:
                    print("存款不能小于等于零！")
                else:
                    account = self.dict_account[self.current_account.accountNumber]
                    account.deposit(deposit_money)
                    self.current_account = account
                    # print(account)
                    print("存款成功！")
            except IOError:
                print("重新输入！")
        pass

    def withdrawal(self):
        if not self.current_account:
            print("请先创建或选择账户！")
        else:
            try:
                withdrawal_money = int(input("请输入取款数额：").strip())
                if withdrawal_money <= 0:
                    print("取款不能小于等于零！")
                else:
                    account = self.dict_account[self.current_account.accountNumber]
                    if account.withdrawal(withdrawal_money):
                        self.current_account = account
                        print(account)
                        print("取款成功！")
                    else:
                        print(f"余额或透支额度不足!")
            except IOError:
                print("重新输入！")
        pass

    def check_account(self):
        if not self.current_account:
            print("请先登录！")
        else:
            for item in self.dict_account.values():
                print(item)
        pass

    def calculate_interest(self):
        if not self.current_account:
            print("请先登录！")
        else:
            if self.current_account.type == "支票":
                print("仅储蓄账户支持该功能！")
            else:
                try:
                    days = int(input("输入利润天数:").strip())
                    account = SavingsAccount(balance=self.current_account.balance)
                    account.calculate_interest(days)
                    print(f"当前余额利息为：{account.balance}")
                except IOError:
                    print("重新输入！")

        pass


def main():
    cli = BankCLI()
    cli.run()


if __name__ == "__main__":
    main()
