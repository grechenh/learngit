from abc import abstractmethod
from datetime import datetime
import re


class Account:
    def __init__(self, accountnumber, accountname, balance=0):
        # self.cont = []
        self.accountNumber = accountnumber
        self.accountName = accountname
        self.balance = balance

    def regist(self, name):
        now = datetime.now()
        account_str = re.findall(r"\d+", str(now))
        account_num = "".join(account_str)
        self.accountName = account_num
        # self.cont.append([account_num,name,0])
        return [account_num, [name, self.balance]]
        pass

    @abstractmethod
    def deposit(self, money):
        # if money < 0:
        #     print("存款金额必须大于0")
        #     return False
        # self.balance += money
        # return True
        return money

    @abstractmethod
    def withdrawal(self, money):
        return money

    def query(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, accountnumber, accountname, balance, yearinterestrate=0.03):
        super().__init__(accountnumber, accountname, balance)
        self.saving_cont = {}
        self.yearInterestRate = yearinterestrate

    def savingregist(self, name):
        saving_account = Account.regist(self, name=name)
        self.saving_cont[saving_account[0]] = saving_account[1]
        return f"储蓄账户创建成功！"
        pass

    def savingdeposit(self, money):
        money = Account.deposit(self, money)
        if money > 0:
            self.saving_cont[self.accountNumber][1] += money
            return
        pass


class CheckingAccount(Account):
    def __init__(self, overdraftlimit):
        self.checking_cont = []
        self.overdraftLimit = overdraftlimit

    def checkingregist(self):
        checking_account = Account.regist()
        self.checking_cont.append(checking_account)
        return f"支票账户创建成功！"





class Showaccount():


    pass



if __name__ == "__main__":

    while True:
        print("....")
        choose = input("").strip()
        if choose == "1":  # 创建账户
            account_name = input("").strip()

            pass
        elif choose == "2":  # 存款

            pass

        elif choose == "3":  # 取款

            pass


        elif choose == "4":  # 查询

            pass

        elif choose == "5":  # 利息计算（仅储蓄账户）

            pass

        elif choose == "6":  # 透支管理（仅支票账户）

            pass

        elif choose == "7":  # 退出
            print("exit success")
            exit()

        else:
            print("error")