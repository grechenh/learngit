from datetime import datetime


class Node:
    def __init__(self, k: int, v: int):
        """单链表(key, value)"""
        self.v = v
        self.k = k
        self.next = None
        self.pre = None


class DoubleList:
    def __init__(self):
        """虚拟头尾"""
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
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
        return  last


class LRUCache:
    def __init__(self, capacity):
        self.cache = DoubleList()
        self.dict = dict()
        self.capacity = capacity
        self.numTimes = None
        self.miss = None

    def get(self, key: int) -> int:
        """拿出库"""
        if key not in self.dict:
            return -1

        # 将该数据提升为最近使用的
        self.makeRecently(key)
        return self.dict[key].v

    def put(self, key: int, val: int) -> None:
        """放入库"""
        if key in self.dict:
            # 删除旧的数据
            self.deleteKey(key)
            # 新插入的数据为最近使用的数据
            self.addRecently(key, val)
            return

        if self.dict == self.cache.size:
            # 删除最久未使用的元素
            self.removeLeastRecently()
        # 添加为最近使用的元素
        self.addRecently(key, val)

    def makeRecently(self, key: int):
        x = self.dict[key]
        # 先从链表中删除这个节点
        self.cache.delValue(x)
        # 重新插到队首
        self.cache.addHead(x)

    def addRecently(self, key: int, val: int):
        x = Node(key, val)
        # 链表头部就是最近使用的元素
        self.cache.addHead(x)
        # 在 哈希表 中添加 key 的映射
        self.dict[key] = x

    def deleteKey(self, key: int):
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

        pass

    def hostProduct(self,num: int):
        if self.cache.head.next == self.cache.tail.pre:
            return f"没有商品！"
        product_list = []
        get_node = list(self.cache)
        get_node.sort(key=lambda x:x.size,reverse=True)
        for _ in range(num):
            product_list.append((get_node.k,get_node.v,get_node.size))
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
        return f"{len(self.dict)}/{self.capacity} "


class Product:
    def __init__(self,sku, name, inventory, capacity, warning_border):
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

    pass





class ProductLIC:
    def __init__(self):
        self.cont = {}
        self.system = Product
        pass

    @staticmethod
    def show():
        """
            1. 查询商品库存
            2. 商品入库
            3. 商品出库
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