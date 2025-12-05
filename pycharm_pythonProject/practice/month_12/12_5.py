import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
import json
import os


class AccountType(Enum):
    """账户类型枚举"""
    SAVINGS = "储蓄账户"
    CHECKING = "支票账户"


class TransactionType(Enum):
    """交易类型枚举"""
    DEPOSIT = "存款"
    WITHDRAW = "取款"
    INTEREST = "利息"
    OVERDRAFT_FEE = "透支费"
    TRANSFER = "转账"


class BankError(Exception):
    """银行账户异常基类"""
    pass


class InsufficientBalanceError(BankError):
    """余额不足异常"""
    pass


class OverdraftLimitExceededError(BankError):
    """透支额度超限异常"""
    pass


class InvalidAmountError(BankError):
    """无效金额异常"""
    pass


class AccountNotFoundError(BankError):
    """账户不存在异常"""
    pass


class Account(ABC):
    """账户基类"""

    def __init__(self, account_number: str, account_holder: str, initial_balance: float = 0.0):
        """
        初始化账户

        Args:
            account_number: 账户号
            account_holder: 户名
            initial_balance: 初始余额
        """
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance
        self.account_type = None
        self.transaction_history = []
        self.created_date = datetime.now()
        self.is_active = True

        # 记录初始交易
        if initial_balance > 0:
            self._record_transaction(TransactionType.DEPOSIT, initial_balance, "初始存款")

    def deposit(self, amount: float) -> bool:
        """
        存款操作

        Args:
            amount: 存款金额

        Returns:
            bool: 操作是否成功

        Raises:
            InvalidAmountError: 存款金额无效
        """
        try:
            if amount <= 0:
                raise InvalidAmountError("存款金额必须大于0")

            self._balance += amount
            self._record_transaction(TransactionType.DEPOSIT, amount, "存款")
            print(f"✅ 存款成功: +${amount:.2f}")
            return True

        except InvalidAmountError as e:
            print(f"❌ 存款失败: {e}")
            return False

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """
        取款操作（抽象方法，子类必须实现）

        Args:
            amount: 取款金额

        Returns:
            bool: 操作是否成功
        """
        pass

    def get_balance(self) -> float:
        """
        查询余额

        Returns:
            float: 当前余额
        """
        return self._balance

    def get_transaction_history(self, count: int = None) -> list:
        """
        获取交易历史

        Args:
            count: 返回的交易记录数量（None表示返回所有）

        Returns:
            list: 交易历史记录
        """
        if count is None:
            return self.transaction_history
        return self.transaction_history[-count:] if self.transaction_history else []

    def _record_transaction(self, transaction_type: TransactionType, amount: float, description: str = ""):
        """记录交易"""
        transaction = {
            'id': str(uuid.uuid4())[:8],
            'timestamp': datetime.now().isoformat(),
            'type': transaction_type.value,
            'amount': amount,
            'balance_after': self._balance,
            'description': description
        }
        self.transaction_history.append(transaction)

    def get_account_info(self) -> dict:
        """获取账户信息"""
        return {
            'account_number': self.account_number,
            'account_holder': self.account_holder,
            'account_type': self.account_type.value if self.account_type else None,
            'balance': self._balance,
            'created_date': self.created_date.strftime('%Y-%m-%d %H:%M:%S'),
            'is_active': self.is_active,
            'transaction_count': len(self.transaction_history)
        }

    def close_account(self) -> bool:
        """关闭账户"""
        if self._balance != 0:
            print("❌ 账户余额不为零，无法关闭")
            return False

        self.is_active = False
        print(f"✅ 账户 {self.account_number} 已关闭")
        return True

    def __str__(self) -> str:
        return (f"账户号: {self.account_number} | 户名: {self.account_holder} | "
                f"类型: {self.account_type.value} | 余额: ${self._balance:.2f}")


class SavingsAccount(Account):
    """储蓄账户子类"""

    def __init__(self, account_number: str, account_holder: str,
                 initial_balance: float = 0.0, annual_interest_rate: float = 0.03):
        """
        初始化储蓄账户

        Args:
            annual_interest_rate: 年利率（默认3%）
        """
        super().__init__(account_number, account_holder, initial_balance)
        self.account_type = AccountType.SAVINGS
        self.annual_interest_rate = annual_interest_rate
        self.last_interest_date = None

    def withdraw(self, amount: float) -> bool:
        """
        取款操作（储蓄账户不允许透支）

        Args:
            amount: 取款金额

        Returns:
            bool: 操作是否成功

        Raises:
            InsufficientBalanceError: 余额不足
            InvalidAmountError: 取款金额无效
        """
        try:
            if amount <= 0:
                raise InvalidAmountError("取款金额必须大于0")

            if amount > self._balance:
                raise InsufficientBalanceError(
                    f"余额不足。当前余额: ${self._balance:.2f}, 尝试取款: ${amount:.2f}"
                )

            self._balance -= amount
            self._record_transaction(TransactionType.WITHDRAW, amount, "取款")
            print(f"✅ 取款成功: -${amount:.2f}")
            return True

        except (InvalidAmountError, InsufficientBalanceError) as e:
            print(f"❌ 取款失败: {e}")
            return False

    def calculate_interest(self, days: int = 30) -> float:
        """
        计算利息

        Args:
            days: 计算利息的天数（默认30天）

        Returns:
            float: 计算的利息金额
        """
        if self._balance <= 0:
            return 0.0

        # 计算日利率
        daily_rate = self.annual_interest_rate / 365

        # 计算利息
        interest = self._balance * daily_rate * days

        return interest

    def apply_interest(self, days: int = 30) -> bool:
        """
        应用利息到账户余额

        Args:
            days: 计算利息的天数

        Returns:
            bool: 操作是否成功
        """
        try:
            interest = self.calculate_interest(days)
            if interest <= 0:
                return False

            self._balance += interest
            self.last_interest_date = datetime.now()
            self._record_transaction(
                TransactionType.INTEREST,
                interest,
                f"{days}天利息（利率: {self.annual_interest_rate * 100:.2f}%）"
            )
            print(f"✅ 利息计算成功: +${interest:.2f}")
            return True

        except Exception as e:
            print(f"❌ 利息计算失败: {e}")
            return False

    def get_account_info(self) -> dict:
        """获取储蓄账户详细信息"""
        info = super().get_account_info()
        info.update({
            'annual_interest_rate': self.annual_interest_rate,
            'last_interest_date': self.last_interest_date.isoformat() if self.last_interest_date else None,
            'daily_interest_rate': self.annual_interest_rate / 365,
            'estimated_monthly_interest': self.calculate_interest(30)
        })
        return info


class CheckingAccount(Account):
    """支票账户子类"""

    def __init__(self, account_number: str, account_holder: str,
                 initial_balance: float = 0.0, overdraft_limit: float = 500.0):
        """
        初始化支票账户

        Args:
            overdraft_limit: 透支额度（默认500元）
        """
        super().__init__(account_number, account_holder, initial_balance)
        self.account_type = AccountType.CHECKING
        self.overdraft_limit = overdraft_limit
        self.overdraft_used = 0.0
        self.overdraft_fee_rate = 0.05  # 5%透支费

    def withdraw(self, amount: float) -> bool:
        """
        取款操作（支票账户允许透支）

        Args:
            amount: 取款金额

        Returns:
            bool: 操作是否成功

        Raises:
            OverdraftLimitExceededError: 透支额度超限
            InvalidAmountError: 取款金额无效
        """
        try:
            if amount <= 0:
                raise InvalidAmountError("取款金额必须大于0")

            # 计算允许的最大取款金额
            available_balance = self._balance + (self.overdraft_limit - self.overdraft_used)

            if amount > available_balance:
                raise OverdraftLimitExceededError(
                    f"取款金额超过可用额度。最大可取: ${available_balance:.2f}, "
                    f"尝试取款: ${amount:.2f}"
                )

            # 执行取款
            self._balance -= amount

            # 更新透支使用情况
            if self._balance < 0:
                new_overdraft = abs(self._balance)
                overdraft_increase = new_overdraft - self.overdraft_used
                if overdraft_increase > 0:
                    self.overdraft_used = new_overdraft

            self._record_transaction(TransactionType.WITHDRAW, amount, "取款")
            print(f"✅ 取款成功: -${amount:.2f}")

            # 检查是否需要收取透支费
            if self._balance < 0 and not self._is_overdraft_fee_applied_today():
                self._apply_overdraft_fee()

            return True

        except (InvalidAmountError, OverdraftLimitExceededError) as e:
            print(f"❌ 取款失败: {e}")
            return False

    def _is_overdraft_fee_applied_today(self) -> bool:
        """检查今天是否已收取过透支费"""
        today = datetime.now().date()
        for transaction in self.transaction_history[-10:]:  # 检查最近10笔交易
            if (transaction['type'] == TransactionType.OVERDRAFT_FEE.value and
                    datetime.fromisoformat(transaction['timestamp']).date() == today):
                return True
        return False

    def _apply_overdraft_fee(self) -> bool:
        """应用透支费"""
        try:
            # 计算透支费（透支金额的5%）
            fee = abs(self._balance) * self.overdraft_fee_rate
            self._balance -= fee
            self._record_transaction(
                TransactionType.OVERDRAFT_FEE,
                fee,
                f"透支费（费率: {self.overdraft_fee_rate * 100:.0f}%）"
            )
            print(f"⚠️  已收取透支费: -${fee:.2f}")
            return True
        except Exception as e:
            print(f"❌ 收取透支费失败: {e}")
            return False

    def get_available_balance(self) -> float:
        """获取可用余额（包括透支额度）"""
        return self._balance + (self.overdraft_limit - self.overdraft_used)

    def get_overdraft_status(self) -> dict:
        """获取透支状态"""
        return {
            'overdraft_limit': self.overdraft_limit,
            'overdraft_used': self.overdraft_used,
            'overdraft_available': self.overdraft_limit - self.overdraft_used,
            'is_overdrawn': self._balance < 0,
            'overdraft_amount': abs(self._balance) if self._balance < 0 else 0.0
        }

    def pay_overdraft(self, amount: float) -> bool:
        """
        偿还透支

        Args:
            amount: 偿还金额

        Returns:
            bool: 操作是否成功
        """
        try:
            if amount <= 0:
                raise InvalidAmountError("偿还金额必须大于0")

            if self._balance >= 0:
                print("ℹ️  账户没有透支")
                return False

            # 计算最大可偿还金额
            max_repayment = abs(self._balance)
            if amount > max_repayment:
                amount = max_repayment

            self._balance += amount
            self.overdraft_used = max(0, self.overdraft_used - amount)

            self._record_transaction(TransactionType.DEPOSIT, amount, "偿还透支")
            print(f"✅ 偿还透支成功: +${amount:.2f}")

            if self._balance >= 0:
                print("✅ 透支已全部还清")

            return True

        except InvalidAmountError as e:
            print(f"❌ 偿还透支失败: {e}")
            return False

    def get_account_info(self) -> dict:
        """获取支票账户详细信息"""
        info = super().get_account_info()
        overdraft_status = self.get_overdraft_status()
        info.update({
            'overdraft_limit': self.overdraft_limit,
            'available_balance': self.get_available_balance(),
            **overdraft_status
        })
        return info


class Bank:
    """银行类，管理所有账户"""

    def __init__(self, name: str = "我的银行"):
        self.name = name
        self.accounts: dict[str, Account] = {}  # account_number -> Account
        self.next_account_number = 100001
        self.data_file = "bank_data.json"
        self._load_data()

    def _generate_account_number(self) -> str:
        """生成账户号"""
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        return account_number

    def create_account(self, account_type: AccountType, account_holder: str,
                       initial_balance: float = 0.0, **kwargs) -> Account:
        """
        创建新账户

        Args:
            account_type: 账户类型
            account_holder: 户名
            initial_balance: 初始余额
            **kwargs: 其他参数（如利率、透支额度等）

        Returns:
            Account: 创建的账户对象
        """
        account_number = self._generate_account_number()

        if account_type == AccountType.SAVINGS:
            interest_rate = kwargs.get('annual_interest_rate', 0.03)
            account = SavingsAccount(account_number, account_holder,
                                     initial_balance, interest_rate)
        elif account_type == AccountType.CHECKING:
            overdraft_limit = kwargs.get('overdraft_limit', 500.0)
            account = CheckingAccount(account_number, account_holder,
                                      initial_balance, overdraft_limit)
        else:
            raise ValueError(f"不支持的账户类型: {account_type}")

        self.accounts[account_number] = account
        self._save_data()

        print(f"✅ 账户创建成功!")
        print(f"   账户号: {account_number}")
        print(f"   户名: {account_holder}")
        print(f"   类型: {account_type.value}")
        print(f"   初始余额: ${initial_balance:.2f}")

        return account

    def get_account(self, account_number: str) -> Account:
        """
        获取账户

        Args:
            account_number: 账户号

        Returns:
            Account: 账户对象

        Raises:
            AccountNotFoundError: 账户不存在
        """
        account = self.accounts.get(account_number)
        if not account:
            raise AccountNotFoundError(f"账户 {account_number} 不存在")
        return account

    def transfer(self, from_account_number: str, to_account_number: str,
                 amount: float) -> bool:
        """
        转账操作

        Args:
            from_account_number: 转出账户
            to_account_number: 转入账户
            amount: 转账金额

        Returns:
            bool: 操作是否成功
        """
        try:
            if from_account_number == to_account_number:
                print("❌ 不能向自己转账")
                return False

            from_account = self.get_account(from_account_number)
            to_account = self.get_account(to_account_number)

            # 从转出账户取款
            if from_account.withdraw(amount):
                # 向转入账户存款
                to_account.deposit(amount)
                from_account._record_transaction(TransactionType.TRANSFER, -amount,
                                                 f"转账到 {to_account_number}")
                to_account._record_transaction(TransactionType.TRANSFER, amount,
                                               f"来自 {from_account_number} 的转账")

                print(f"✅ 转账成功!")
                print(f"   从: {from_account_number} ({from_account.account_holder})")
                print(f"   到: {to_account_number} ({to_account.account_holder})")
                print(f"   金额: ${amount:.2f}")

                self._save_data()
                return True

            return False

        except AccountNotFoundError as e:
            print(f"❌ 转账失败: {e}")
            return False
        except Exception as e:
            print(f"❌ 转账失败: {e}")
            return False

    def get_bank_summary(self) -> dict:
        """获取银行摘要信息"""
        total_balance = sum(acc.get_balance() for acc in self.accounts.values())
        active_accounts = sum(1 for acc in self.accounts.values() if acc.is_active)

        savings_accounts = [acc for acc in self.accounts.values()
                            if isinstance(acc, SavingsAccount)]
        checking_accounts = [acc for acc in self.accounts.values()
                             if isinstance(acc, CheckingAccount)]

        return {
            'bank_name': self.name,
            'total_accounts': len(self.accounts),
            'active_accounts': active_accounts,
            'total_balance': total_balance,
            'savings_accounts_count': len(savings_accounts),
            'checking_accounts_count': len(checking_accounts),
            'savings_total_balance': sum(acc.get_balance() for acc in savings_accounts),
            'checking_total_balance': sum(acc.get_balance() for acc in checking_accounts)
        }

    def _save_data(self):
        """保存数据到文件"""
        try:
            data = {
                'next_account_number': self.next_account_number,
                'accounts': []
            }

            for account in self.accounts.values():
                account_data = account.get_account_info()
                account_data['transaction_history'] = account.transaction_history

                # 添加子类特定数据
                if isinstance(account, SavingsAccount):
                    account_data['annual_interest_rate'] = account.annual_interest_rate
                    account_data[
                        'last_interest_date'] = account.last_interest_date.isoformat() if account.last_interest_date else None
                elif isinstance(account, CheckingAccount):
                    account_data['overdraft_limit'] = account.overdraft_limit
                    account_data['overdraft_used'] = account.overdraft_used
                    account_data['overdraft_fee_rate'] = account.overdraft_fee_rate

                data['accounts'].append(account_data)

            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

        except Exception as e:
            print(f"⚠️  保存数据失败: {e}")

    def _load_data(self):
        """从文件加载数据"""
        try:
            if not os.path.exists(self.data_file):
                return

            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.next_account_number = data['next_account_number']

            for account_data in data['accounts']:
                account_type = account_data['account_type']
                account_number = account_data['account_number']
                account_holder = account_data['account_holder']
                balance = account_data['balance']

                if account_type == AccountType.SAVINGS.value:
                    interest_rate = account_data.get('annual_interest_rate', 0.03)
                    account = SavingsAccount(account_number, account_holder,
                                             balance, interest_rate)
                elif account_type == AccountType.CHECKING.value:
                    overdraft_limit = account_data.get('overdraft_limit', 500.0)
                    account = CheckingAccount(account_number, account_holder,
                                              balance, overdraft_limit)
                    account.overdraft_used = account_data.get('overdraft_used', 0.0)
                    account.overdraft_fee_rate = account_data.get('overdraft_fee_rate', 0.05)
                else:
                    continue

                # 恢复交易历史
                account.transaction_history = account_data.get('transaction_history', [])
                account.is_active = account_data.get('is_active', True)

                # 恢复储蓄账户的利息日期
                if isinstance(account, SavingsAccount):
                    last_interest_date = account_data.get('last_interest_date')
                    if last_interest_date:
                        account.last_interest_date = datetime.fromisoformat(last_interest_date)

                self.accounts[account_number] = account

            print(f"✅ 已加载 {len(self.accounts)} 个账户")

        except Exception as e:
            print(f"⚠️  加载数据失败: {e}")


class BankCLI:
    """银行系统命令行界面"""

    def __init__(self):
        self.bank = Bank("智慧银行系统")
        self.current_account = None

    def display_menu(self):
        """显示主菜单"""
        print("\n" + "=" * 50)
        print("🏦 银行账户管理系统")
        print("=" * 50)

        if self.current_account:
            print(f"当前账户: {self.current_account.account_number} "
                  f"({self.current_account.account_holder})")
            print(f"余额: ${self.current_account.get_balance():.2f}")

            if isinstance(self.current_account, CheckingAccount):
                overdraft_info = self.current_account.get_overdraft_status()
                print(f"透支额度: ${overdraft_info['overdraft_limit']:.2f}")
                print(f"可用透支: ${overdraft_info['overdraft_available']:.2f}")

        print("\n请选择操作:")
        print("1. 创建新账户")
        print("2. 选择账户")
        print("3. 存款")
        print("4. 取款")
        print("5. 查询余额")
        print("6. 查看交易历史")
        print("7. 计算利息（储蓄账户）")
        print("8. 查看透支情况（支票账户）")
        print("9. 转账")
        print("10. 查看账户信息")
        print("11. 银行摘要")
        print("12. 关闭账户")
        print("0. 退出系统")
        print("=" * 50)

    def run(self):
        """运行命令行界面"""
        print("🚀 欢迎使用银行账户管理系统!")

        while True:
            self.display_menu()

            try:
                choice = input("\n请输入选项 (0-12): ").strip()

                if choice == "0":
                    print("👋 感谢使用，再见!")
                    break
                elif choice == "1":
                    self.create_account()
                elif choice == "2":
                    self.select_account()
                elif choice == "3":
                    self.deposit()
                elif choice == "4":
                    self.withdraw()
                elif choice == "5":
                    self.check_balance()
                elif choice == "6":
                    self.view_transactions()
                elif choice == "7":
                    self.calculate_interest()
                elif choice == "8":
                    self.view_overdraft()
                elif choice == "9":
                    self.transfer()
                elif choice == "10":
                    self.view_account_info()
                elif choice == "11":
                    self.view_bank_summary()
                elif choice == "12":
                    self.close_account()
                else:
                    print("❌ 无效选项，请重新输入")

            except KeyboardInterrupt:
                print("\n\n👋 用户中断，退出系统")
                break
            except Exception as e:
                print(f"❌ 发生错误: {e}")

    def create_account(self):
        """创建新账户"""
        print("\n📝 创建新账户")
        print("-" * 30)

        # 获取账户类型
        print("请选择账户类型:")
        print("1. 储蓄账户 (有利息)")
        print("2. 支票账户 (可透支)")

        type_choice = input("请输入选项 (1/2): ").strip()
        if type_choice == "1":
            account_type = AccountType.SAVINGS
        elif type_choice == "2":
            account_type = AccountType.CHECKING
        else:
            print("❌ 无效选择")
            return

        # 获取户名
        account_holder = input("请输入户名: ").strip()
        if not account_holder:
            print("❌ 户名不能为空")
            return

        # 获取初始余额
        try:
            initial_balance = float(input("请输入初始余额 (默认0): ").strip() or "0")
            if initial_balance < 0:
                print("❌ 初始余额不能为负数")
                return
        except ValueError:
            print("❌ 请输入有效的数字")
            return

        # 根据账户类型获取额外参数
        kwargs = {}
        if account_type == AccountType.SAVINGS:
            try:
                interest_rate = float(input("请输入年利率 (默认3%, 输入如0.03): ").strip() or "0.03")
                kwargs['annual_interest_rate'] = interest_rate
            except ValueError:
                print("❌ 请输入有效的利率")
                return
        elif account_type == AccountType.CHECKING:
            try:
                overdraft_limit = float(input("请输入透支额度 (默认500): ").strip() or "500")
                kwargs['overdraft_limit'] = overdraft_limit
            except ValueError:
                print("❌ 请输入有效的透支额度")
                return

        # 创建账户
        account = self.bank.create_account(account_type, account_holder,
                                           initial_balance, **kwargs)
        self.current_account = account

    def select_account(self):
        """选择账户"""
        if not self.bank.accounts:
            print("❌ 系统中暂无账户")
            return

        print("\n📋 账户列表:")
        print("-" * 60)
        print(f"{'账户号':<12} {'户名':<10} {'类型':<8} {'余额':<12} {'状态'}")
        print("-" * 60)

        for account in self.bank.accounts.values():
            status = "活跃" if account.is_active else "已关闭"
            print(f"{account.account_number:<12} {account.account_holder:<10} "
                  f"{account.account_type.value:<8} ${account.get_balance():<11.2f} {status}")

        account_number = input("\n请输入要选择的账户号: ").strip()

        try:
            self.current_account = self.bank.get_account(account_number)
            print(f"✅ 已选择账户: {account_number}")
        except AccountNotFoundError as e:
            print(f"❌ {e}")

    def deposit(self):
        """存款操作"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        try:
            amount = float(input("请输入存款金额: ").strip())
            self.current_account.deposit(amount)
        except ValueError:
            print("❌ 请输入有效的数字")
        except InvalidAmountError as e:
            print(f"❌ {e}")

    def withdraw(self):
        """取款操作"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        try:
            amount = float(input("请输入取款金额: ").strip())
            self.current_account.withdraw(amount)
        except ValueError:
            print("❌ 请输入有效的数字")
        except (InsufficientBalanceError, OverdraftLimitExceededError, InvalidAmountError) as e:
            print(f"❌ {e}")

    def check_balance(self):
        """查询余额"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        balance = self.current_account.get_balance()
        print(f"\n💰 账户余额: ${balance:.2f}")

        if isinstance(self.current_account, CheckingAccount):
            available = self.current_account.get_available_balance()
            print(f"💳 可用余额 (含透支): ${available:.2f}")

    def view_transactions(self):
        """查看交易历史"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        transactions = self.current_account.get_transaction_history()

        if not transactions:
            print("📭 暂无交易记录")
            return

        print(f"\n📊 交易记录 (共{len(transactions)}笔):")
        print("=" * 80)
        print(f"{'时间':<20} {'类型':<8} {'金额':<12} {'余额':<12} {'描述'}")
        print("-" * 80)

        for t in transactions[-20:]:  # 显示最近20笔
            time_str = datetime.fromisoformat(t['timestamp']).strftime('%Y-%m-%d %H:%M')
            amount = t['amount']
            amount_str = f"+${amount:.2f}" if amount >= 0 else f"-${abs(amount):.2f}"

            print(f"{time_str:<20} {t['type']:<8} {amount_str:<12} "
                  f"${t['balance_after']:<11.2f} {t.get('description', '')}")

    def calculate_interest(self):
        """计算利息（储蓄账户）"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        if not isinstance(self.current_account, SavingsAccount):
            print("❌ 只有储蓄账户可以计算利息")
            return

        try:
            days = int(input("请输入计算利息的天数 (默认30): ").strip() or "30")
            interest = self.current_account.calculate_interest(days)

            print(f"\n📈 利息计算:")
            print(f"   本金: ${self.current_account.get_balance():.2f}")
            print(f"   年利率: {self.current_account.annual_interest_rate * 100:.2f}%")
            print(f"   天数: {days}天")
            print(f"   利息: ${interest:.2f}")

            apply = input("\n是否将利息应用到账户余额? (y/N): ").strip().lower()
            if apply == 'y':
                self.current_account.apply_interest(days)

        except ValueError:
            print("❌ 请输入有效的数字")

    def view_overdraft(self):
        """查看透支情况"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        if not isinstance(self.current_account, CheckingAccount):
            print("❌ 只有支票账户有透支功能")
            return

        overdraft_info = self.current_account.get_overdraft_status()

        print("\n💳 透支情况:")
        print(f"   透支额度: ${overdraft_info['overdraft_limit']:.2f}")
        print(f"   已用透支: ${overdraft_info['overdraft_used']:.2f}")
        print(f"   可用透支: ${overdraft_info['overdraft_available']:.2f}")

        if overdraft_info['is_overdrawn']:
            print(f"   ⚠️  当前透支: ${overdraft_info['overdraft_amount']:.2f}")

            repay = input("\n是否偿还透支? (y/N): ").strip().lower()
            if repay == 'y':
                try:
                    amount = float(input("请输入偿还金额: ").strip())
                    self.current_account.pay_overdraft(amount)
                except ValueError:
                    print("❌ 请输入有效的数字")
                except InvalidAmountError as e:
                    print(f"❌ {e}")

    def transfer(self):
        """转账"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        try:
            to_account = input("请输入转入账户号: ").strip()
            amount = float(input("请输入转账金额: ").strip())

            self.bank.transfer(self.current_account.account_number, to_account, amount)
        except ValueError:
            print("❌ 请输入有效的数字")
        except AccountNotFoundError as e:
            print(f"❌ {e}")

    def view_account_info(self):
        """查看账户信息"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        info = self.current_account.get_account_info()

        print("\n📋 账户详细信息:")
        print("-" * 40)
        for key, value in info.items():
            if key not in ['transaction_history', 'transaction_count']:
                print(f"{key.replace('_', ' ').title():<20}: {value}")

    def view_bank_summary(self):
        """查看银行摘要"""
        summary = self.bank.get_bank_summary()

        print("\n🏦 银行系统摘要:")
        print("=" * 40)
        for key, value in summary.items():
            if 'balance' in key:
                print(f"{key.replace('_', ' ').title():<25}: ${value:.2f}")
            else:
                print(f"{key.replace('_', ' ').title():<25}: {value}")

    def close_account(self):
        """关闭账户"""
        if not self.current_account:
            print("❌ 请先选择账户")
            return

        confirm = input(f"确定要关闭账户 {self.current_account.account_number} 吗? (y/N): ").strip().lower()
        if confirm == 'y':
            if self.current_account.close_account():
                self.current_account = None


def main():
    """主函数"""
    try:
        cli = BankCLI()
        cli.run()
    except Exception as e:
        print(f"❌ 系统发生错误: {e}")
        input("按Enter键退出...")


if __name__ == "__main__":
    main()