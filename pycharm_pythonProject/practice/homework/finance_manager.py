# from pathlib import Path

class FinanceManager:
    def __init__(self):
        self.cont = []
        pass

    def add_transaction(self, amount, category, description):
        """添加交易记录"""
        dict_cunt = {"金额": amount,
                     "类别": category,
                     "描述": description,
                     "type": "收入" if amount > 0 else "支出"
                     }
        self.cont.append(dict_cunt)
        get_type = "收入" if amount > 0 else "支出"
        return f"{get_type}添加成功！"

    def get_balance(self):
        """计算并返回当前余额"""
        result = sum(item["金额"] for item in self.cont)
        return result

    def get_summary_by_category(self, category):
        """按类别汇总交易金额"""
        list_cont = []
        for i in self.cont:
            if i["类别"] == category:
                dict_cunt = {"金额": i["金额"],
                             "描述": i["描述"]
                             }
                list_cont.append(dict_cunt)
        # print(self.cont)
        # print(list_cont)
        return list_cont

    # def save_to_file(self, filename):
    #     """用于数据持久化"""
    #     # 创建文件夹
    #     folder = Path("new_folder")
    #     folder.mkdir()
    #
    #     # 写入文件
    #     file_path = folder.joinpath("FinanceManger.txt")
    #     with open(file_path, "w") as file:
    #         file.write(self.cont)
    #     pass
    #
    # def load_from_file(self):
    #     """用于数据持久化"""
    #
    #     pass


if __name__ == "__main__":
    manager = FinanceManager()
    while True:
        print("\n\n1. 添加收入 2. 添加支出 3. 查看余额 4. 查看分类汇总 5. 保存数据 6. 加载数据 7. 退出")
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
            end = manager.add_transaction(amount=amount, category=category, description=description)
            print(end)
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
                end = manager.add_transaction(amount=amount, category=category, description=description)
                print(end)
        elif choose == "3":
            end = manager.get_balance()
            print(f"余额为：{end}")
            pass
        elif choose == "4":
            category = input("请输入类别：")
            end = manager.get_summary_by_category(category)
            if len(end) == 0:
                print("没有该类型！")
                continue
            for i in end:
                print(f"类别：{category} 金额：{i['金额']} 描述:{i['描述']}")
            pass
        # elif choose == "5":
        #
        #     pass
        # elif choose == "6":
        #
        #     pass
        elif choose == "7":
            exit()
        else:
            print("error")
