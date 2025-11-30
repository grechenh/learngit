class FinanceManager:
    def __init__(self, cont):
        self.cont = []
        pass

    def add_transaction(self, amount, category, description):
        """添加交易记录"""
        dict_cunt = {"金额": amount,
                     "类别": category,
                     "描述": description,
                     "type":"收入" if amount > 0 else "支出"
                     }
        self.cont.append(dict_cunt)
        type = "收入" if amount > 0 else "支出"
        return f"{type}添加成功！"

    def get_balance(self):
        """计算并返回当前余额"""
        result = sum(item["金额"] for item in self.cont)
        return result

    def get_summary_by_category(self):
        """按类别汇总交易金额"""
        list_cont = []
        for i in self.cont:
            if i["类别"] not in list_cont:
                dict_cont["类别"] = i["类别"]
                dict_cont["金额"] = i["金额"]
            else:
                dict_cont["金额"] += i["金额"]
        return dict_cont

    def save_to_file(self, filename):
        """用于数据持久化"""

        pass

    def load_from_file(self):
        """用于数据持久化"""

        pass


def main():
    while True:
        print("1. 添加收入 2. 添加支出 3. 查看余额 4. 查看分类汇总 5. 保存数据 6. 加载数据 7. 退出")
        print("请选择: ")
        choose = input().strip()
        if choose == "1":
            try:
                amount = float(input("请输入金额：").strip())
            except ValueError:
                print("请输入有效数字！")
                continue
            category = input("请输入类别：")
            description = input("请输入描述：")
            FinanceManager(amount=amount, category=category, description=description)
            print("收入添加成功！")

        elif choose == "2":
            try:
                amount = float(input("请输入金额：").strip())
            except ValueError:
                print("请输入有效数字！")
                continue
            if amount > 0:
                print("支出金额应该为负数！！")
            else:
                category = input("请输入类别：")
                description = input("请输入描述：")

                print("支出添加成功！")
        elif choose == "3":
            pass
        elif choose == "4":
            pass
        elif choose == "5":
            pass
        elif choose == "6":
            pass
        elif choose == "7":
            exit()
        else:
            print("error")