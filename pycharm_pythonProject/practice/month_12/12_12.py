from datetime import datetime


class Node:
    def __init__(self, k: str, v: int):
        """单链表(key, value)"""
        self.v = v
        self.k = k
        self.next = None
        self.pre = None


class DoubleList:
    def __init__(self):
        """虚拟头尾"""
        self.head = Node("", 0)
        self.tail = Node("", 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    pass

    def addHead(self, x: Node):
        """从头部添加节点"""
        x.next = self.head.next
        x.pre = self.head
        self.head.next.pre = x
        self.head.next = x
        self.size += 1
        pass

    def delValue(self, x: Node):
        """删除列表第x节点"""
        x.pre.next = x.next
        x.next.pre = x.pre
        self.size -= 1
        pass

    def delTail(self):
        """删除尾节点"""
        if self.tail == self.head:
            return None
        last = self.tail.pre
        self.delValue(last)
        return last


class LRUCache:
    def __init__(self, capacity=100):
        self.cache = DoubleList()
        self.dict = dict()
        self.capacity = capacity
        self.miss = 0
        self.hit = 0

    def get(self, key: str) -> int:
        """拿出库"""
        if key not in self.dict:
            self.miss += 1
            return -1

        # 将该数据提升为最近使用的
        self.makeRecently(key)
        self.hit += 1
        return self.dict[key].v

    def put(self, key: str, val: int) -> None:
        """放入库"""
        if key in self.dict:
            # 删除旧的数据
            self.deleteKey(key)
            # 新插入的数据为最近使用的数据
            self.addRecently(key, val)
            self.hit += 1
            return

        if self.capacity == self.cache.size:
            # 删除最久未使用的元素
            self.removeLeastRecently()
        # 添加为最近使用的元素
        self.addRecently(key, val)
        self.miss += 1

    def query(self, key: str):
        get_val = self.dict[key]
        pass

    def makeRecently(self, key: str):
        x = self.dict[key]
        # 先从链表中删除这个节点
        self.cache.delValue(x)
        # 重新插到队首
        self.cache.addHead(x)

    def addRecently(self, key: str, val: int):
        x = Node(key, val)
        # 链表头部就是最近使用的元素
        self.cache.addHead(x)
        # 在 哈希表 中添加 key 的映射
        self.dict[key] = x

    def deleteKey(self, key: str):
        x = self.dict[key]
        # 从链表中删除
        self.cache.delValue(x)
        # 从 哈希表 中删除
        self.dict.pop(key)

    def removeLeastRecently(self):
        # 链表尾部的第一个元素就是最久未使用的
        deletedNode = self.cache.delTail()
        # 从 哈希表 中删除它的 key
        deletedKey = deletedNode.k
        self.dict.pop(deletedKey)

    def cacheRate(self):
        total = self.miss + self.hit
        return self.hit / total * 100 if total > 0 else 0
        pass

    def hostProduct(self, num: int = 5):
        if self.cache.head.next == self.cache.tail.pre:
            return f"没有商品！"
        product_list = []
        get_node = list(self.cache)
        get_node.sort(key=lambda x: x.size, reverse=True)
        for _ in range(num):
            product_list.append((get_node.k, get_node.v, get_node.size))
            get_node = get_node.next
        return product_list

    def cacheInformation(self):
        """
        LRU缓存状态:
        缓存容量: 100/100
        缓存命中率: 95.3%
        热门商品:
        1. PROD001 - iPhone 15 (访问次数: 1250)
        2. PROD003 - AirPods Pro (访问次数: 980)
        3. PROD002 - MacBook Pro (访问次数: 850)
        """
        return f"{len(self.dict)}/{self.capacity}\n{self.cacheRate()}%"


class Product:
    def __init__(self, sku, name, inventory, warning_border, capacity=100):
        self.LRU = LRUCache(capacity)
        self.sku = sku
        self.name = name
        self.inventory = inventory
        self.warningBorder = warning_border
        self.creatTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pass

    def __str__(self):
        """商品SKU: PROD001 | 名称: iPhone 15 | 库存: 150 | 预警阈值: 20"""
        return f"商品SKU:{self.sku} | 名称:{self.name} | 库存: {self.inventory} | 预警阈值:{self.warningBorder}"

    def update_quantity(self, num: int):
        self.inventory += num
        self.updateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pass

    def check_warning(self):
        if self.inventory <= self.warningBorder:
            return False
        return True


class ProductSystem:
    def __init__(self, cache_capacity: int = 100):
        self.cache = LRUCache(cache_capacity)
        self.inventory: dict[str, Product] = {}
        self.operation_history = dict()
        self.warnings = []

    def add_product(self, sku, name, inventory, warning_border, capacity=100):
        if sku in self.inventory:
            raise ValueError(f"商品 {sku} 已存在")
        item = Product(sku, name, inventory, warning_border, capacity)
        self.inventory[sku] = item
        self.cache.put(sku, inventory)

    pass


class ProductLIC:
    def __init__(self):
        self.cont = {}
        self.system = ProductSystem()
        pass

    def initOperate(self):
        # 初始化一些商品
        print("=== 初始化库存系统 ===")
        initial_products = [
            ("PROD001", "iPhone 15", 150, 20, 6999.00),
            ("PROD002", "MacBook Pro", 80, 10, 12999.00),
            ("PROD003", "AirPods Pro", 300, 50, 1899.00),
            ("PROD004", "iPad Air", 120, 30, 4799.00),
            ("PROD005", "Apple Watch", 200, 40, 2999.00),
        ]

        for sku, name, qty, threshold, price in initial_products:
            self.system.add_product(sku, name, qty, threshold, price)
            print(f"添加商品: {name} (SKU: {sku}) 库存: {qty}")

        # 模拟一些访问
        print("\n模拟用户访问热门商品...")
        for _ in range(100):
            self.system.get_product("PROD001")  # iPhone 15 - 热门商品
            self.system.get_product("PROD003")  # AirPods Pro - 热门商品

        for _ in range(50):
            self.system.get_product("PROD002")  # MacBook Pro

    @staticmethod
    def show():
        """
            1. 查询商品库存
            3. 商品出库
            2. 商品入库
            4. 查看LRU缓存状态
            5. 查看库存预警
            6. 查看缓存命中率
            7. 查看操作历史
            8. 退出
        """
        print("\n" + "=" * 50)
        print("🏦 电商库存管理系统")
        print("=" * 50)
        print("1.查询商品库存   2.商品入库    3.商品出库    4.查看LRU缓存状态  \n5.查看库存预警    6.查看缓存命中率   7.查看操作历史   0.退出 ")

    pass

    def run(self):
        while True:
            self.show()
            try:
                choose = input("\n请输入选项(0-7)：").strip()
                if choose == "1":
                    # 查询商品库存
                    self.query_product()
                elif choose == "2":
                    # 商品入库
                    self.put_product()
                elif choose == "3":
                    # 商品出库
                    self.get_product()
                elif choose == "4":
                    # 查看LRU缓存状态
                    self.query_LRU()
                elif choose == "5":
                    # 查看库存预警
                    self.query_warning()
                elif choose == "6":
                    # 查看缓存命中率
                    self.query_cache_rate()
                elif choose == "7":
                    # 查看操作历史
                    self.query_operate_history()
                elif choose == "0":
                    # 退出
                    print("exit success")
                    exit()
                else:
                    print("error")
            except KeyboardInterrupt:
                print("\n系统中断！")
                break
        pass

    def query_product(self):

        pass

    pass


if __name__ == '__main__':
    pass
