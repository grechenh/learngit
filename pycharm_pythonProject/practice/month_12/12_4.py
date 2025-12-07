from abc import abstractmethod
from datetime import datetime
import re
from enum import Enum


class AccountType(Enum):
    """商品类型枚举"""
    SAVING = "储蓄账户"
    CHECKING = "支票账户"


class Account:
    def __init__(self, number=None, name=None, balance=0):
        self.account_list = []
        self.accountNumber = number
        self.accountName = name
        self.balance = balance

    # def __str__(self):
    #     return f"账户：{self.accountNumber} 账号名：{self.accountName} 余额：{self.balance}"

    @abstractmethod
    def register(self, name):
        now = datetime.now()
        account_str = re.findall(r"\d+", str(now))
        account_num = "".join(account_str)
        self.accountNumber = account_num
        self.cont[self.accountNumber] = [name, self.balance]

    @abstractmethod
    def deposit(self, money):
        self.balance += money

    @abstractmethod
    def withdrawal(self, lose_money):
        self.balance -= lose_money

    @abstractmethod
    def query(self):
        return self.account_list


class SavingsAccount(Account):
    def __init__(self, number=None, name=None, balance=0, year_interest_rate=0.03):
        super().__init__(number, name, balance)
        self.yearInterestRate = year_interest_rate
        self.type = AccountType.SAVING

    def __str__(self):
        return f"账户：{self.accountNumber} 账号名：{self.accountName} 余额：{self.balance} 类型：{self.type}"

    def saving_register(self, name):
        now = datetime.now()
        account_str = re.findall(r"\d+", str(now))
        account_num = "".join(account_str)
        self.accountNumber = account_num
        self.accountName = name
        self.account_list[self.accountNumber] = [self.accountName, self.balance, self.type]
        return [self.accountNumber, name, self.balance]

    # def savingdeposit(self, money):
    #     money = Account.deposit(self, money)
    #     if money > 0:
    #         self.cont[self.accountNumber][1] += money
    #         return
    #     pass


class CheckingAccount(Account):
    def __init__(self, overdraft_limit=500):
        super().__init__()
        self.overdraftLimit = overdraft_limit
        self.type = AccountType.CHECKING

    def checking_register(self, name):
        now = datetime.now()
        account_str = re.findall(r"\d+", str(now))
        account_num = "".join(account_str)
        self.accountNumber = account_num
        self.accountNumber = name
        self.cont[self.accountNumber] = [name, self.balance, self.type]
        return [self.accountNumber, name, self.balance]

    # def


class BankCLI:
    def __init__(self):
        self.current_account = None
        pass

    def show(self):
        """显示主菜单"""
        print("\n" + "=" * 50)
        print("🏦 银行账户管理系统")
        print("=" * 50)
        if self.current_account:
            print(f"当前账户: {self.current_account[0]}({self.current_account[1]}) ")
            print(f"余额: ${self.current_account[2]:.2f}\n")
        print("1.创建账户    2.存款    3.取款    4.查询\n5.利息计算（仅储蓄账户） 6.透支管理（仅支票账户） 0.退出 ")

    def run(self):
        while True:
            self.show()
            try:
                choose = input("\n请输入选项(0-6)：").strip()
                if choose == "1":  # 创建账户
                    self.create_count()
                elif choose == "2":  # 存款
                    self.deposit_account()
                elif choose == "3":  # 取款
                    self.withdrawal()
                elif choose == "4":  # 查询
                    self.check_account()
                elif choose == "5":  # 利息计算（仅储蓄账户）
                    self.calculate_interest()
                elif choose == "6":  # 透支管理（仅支票账户）
                    self.view_overdraft()
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
        if get_type == "1":
            s_create = SavingsAccount()
            self.current_account = s_create.saving_register(name=account_name)
            print(s_create)
        elif get_type == "2":
            # now = datetime.now()
            # account_str = re.findall(r"\d+", str(now))
            # account_num = "".join(account_str)
            # c_create = CheckingAccount()
            # c_create.checking_cont[c_create.accountNumber] = [c_create.accountName, c_create.balance]
            # self.current_account = c_create.checking_cont[c_create.accountNumber]
            # print(c_create)
            c_create = CheckingAccount()
            self.current_account = c_create.checking_register(name=account_name)
            print(c_create)
        else:
            print("重新输入！")
        pass

    def deposit_account(self):
        if not self.current_account:
            print("请先创建账户！")
        else:
            s = Account()
            print(s)
        pass

    def withdrawal(self):

        pass

    def check_account(self):

        pass

    def calculate_interest(self):
        if self.current_account[2] == "支票":
            print("仅储蓄账户支持该功能！")
        # else:

        pass

    def view_overdraft(self):
        if self.current_account[2] == "储蓄":
            print("仅支票账户支持该功能！")
        # else:

        pass


def main():
    cli = BankCLI()
    cli.run()


if __name__ == "__main__":
    main()
