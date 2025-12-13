# class Node:
#     def __init__(self, k, v):
#         self.key = k
#         self.val = v
#         self.next = None
#         self.prev = None
#
#
# class DoubleList:
#     def __init__(self):
#         # 头尾虚节点
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         # 链表元素数
#         self._size = 0
#
#         # 初始化双向链表的数据
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     # 在链表尾部添加节点 x，时间 O(1)
#     def addLast(self, x):
#         x.prev = self.tail.prev
#         x.next = self.tail
#         self.tail.prev.next = x
#         self.tail.prev = x
#         self._size += 1
#
#     # 删除链表中的 x 节点（x 一定存在）
#     # 由于是双链表且给的是目标 Node 节点，时间 O(1)
#     def remove(self, x):
#         x.prev.next = x.next
#         x.next.prev = x.prev
#         self._size -= 1
#
#     # 删除链表中第一个节点，并返回该节点，时间 O(1)
#     def removeFirst(self):
#         if self.head.next == self.tail:
#             return None
#         first = self.head.next
#         self.remove(first)
#         return first
#
#     # 返回链表长度，时间 O(1)
#     def size(self):
#         return self._size
#
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         # key -> Node(key, val)
#         self.map = {}
#         # Node(k1, v1) <-> Node(k2, v2)...
#         self.cache = DoubleList()
#         # 最大容量
#         self.cap = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self.map:
#             return -1
#
#         # 将该数据提升为最近使用的
#         self.makeRecently(key)
#         return self.map[key].val
#
#     def put(self, key: int, val: int) -> None:
#         if key in self.map:
#             # 删除旧的数据
#             self.deleteKey(key)
#             # 新插入的数据为最近使用的数据
#             self.addRecently(key, val)
#             return
#
#         if self.cap == self.cache.size():
#             # 删除最久未使用的元素
#             self.removeLeastRecently()
#         # 添加为最近使用的元素
#         self.addRecently(key, val)
#
#     def makeRecently(self, key: int):
#         x = self.map[key]
#         # 先从链表中删除这个节点
#         self.cache.remove(x)
#         # 重新插到队尾
#         self.cache.addLast(x)
#
#     def addRecently(self, key: int, val: int):
#         x = Node(key, val)
#         # 链表尾部就是最近使用的元素
#         self.cache.addLast(x)
#         # 别忘了在 map 中添加 key 的映射
#         self.map[key] = x
#
#     def deleteKey(self, key: int):
#         x = self.map[key]
#         # 从链表中删除
#         self.cache.remove(x)
#         # 从 map 中删除
#         self.map.pop(key)
#
#     def removeLeastRecently(self):
#         # 链表头部的第一个元素就是最久未使用的
#         deletedNode = self.cache.removeFirst()
#         # 同时别忘了从 map 中删除它的 key
#         deletedKey = deletedNode.key
#         self.map.pop(deletedKey)
#
#
#
import random

import threading
import time
from datetime import datetime
from typing import Optional, Dict, Any
from collections import OrderedDict


class LRUCacheNode:
    """LRU缓存节点"""

    def __init__(self, key: str, value: Any):
        self.key = key
        self.value = value
        self.prev: Optional[LRUCacheNode] = None
        self.next: Optional[LRUCacheNode] = None
        self.access_count = 0
        self.last_accessed = datetime.now()


class LRUCache:
    """LRU缓存实现（双向链表 + 哈希表）"""

    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.cache: Dict[str, LRUCacheNode] = {}
        self.head = LRUCacheNode(None, None)  # 虚拟头节点
        self.tail = LRUCacheNode(None, None)  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = threading.Lock()
        self.hits = 0
        self.misses = 0

    def _add_to_head(self, node: LRUCacheNode):
        """将节点添加到链表头部"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: LRUCacheNode):
        """从链表中移除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: LRUCacheNode):
        """将节点移动到头部"""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        """移除尾部节点"""
        if self.tail.prev != self.head:
            node = self.tail.prev
            self._remove_node(node)
            return node
        return None

    def get(self, key: str) -> Optional[Any]:
        """获取缓存值"""
        with self.lock:
            if key not in self.cache:
                self.misses += 1
                return None

            node = self.cache[key]
            node.access_count += 1
            node.last_accessed = datetime.now()
            self._move_to_head(node)
            self.hits += 1
            return node.value

    def put(self, key: str, value: Any):
        """添加缓存"""
        with self.lock:
            if key in self.cache:
                # 更新现有节点
                node = self.cache[key]
                node.value = value
                node.access_count += 1
                node.last_accessed = datetime.now()
                self._move_to_head(node)
            else:
                # 创建新节点
                node = LRUCacheNode(key, value)
                self.cache[key] = node
                self._add_to_head(node)

                # 如果超过容量，移除最久未使用的
                if len(self.cache) > self.capacity:
                    removed = self._remove_tail()
                    if removed:
                        del self.cache[removed.key]

    def remove(self, key: str):
        """移除缓存"""
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                self._remove_node(node)
                del self.cache[key]

    def get_hit_rate(self) -> float:
        """获取缓存命中率"""
        total = self.hits + self.misses
        return (self.hits / total * 100) if total > 0 else 0

    def get_top_items(self, count: int = 10):
        """获取最热门的商品"""
        with self.lock:
            items = list(self.cache.values())
            items.sort(key=lambda x: x.access_count, reverse=True)
            return [(item.key, item.value, item.access_count)
                    for item in items[:count]]

    def get_cache_info(self):
        """获取缓存信息"""
        with self.lock:
            return {
                'capacity': self.capacity,
                'current_size': len(self.cache),
                'hits': self.hits,
                'misses': self.misses,
                'hit_rate': f"{self.get_hit_rate():.1f}%"
            }


class InventoryItem:
    """库存商品类"""

    def __init__(self, sku: str, name: str, quantity: int,
                 warning_threshold: int = 10, price: float = 0.0):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.warning_threshold = warning_threshold
        self.price = price
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_quantity(self, delta: int):
        """更新库存数量"""
        self.quantity += delta
        self.updated_at = datetime.now()

    def check_warning(self) -> bool:
        """检查是否需要预警"""
        return self.quantity <= self.warning_threshold

    def __str__(self):
        status = "⚠️ 需要补货" if self.check_warning() else "✓ 正常"
        return (f"SKU: {self.sku} | 名称: {self.name} | "
                f"库存: {self.quantity} | 预警: {self.warning_threshold} | 状态: {status}")


class InventoryOperation:
    """库存操作记录"""

    def __init__(self, sku: str, operation_type: str,
                 quantity: int, operator: str = "System"):
        self.sku = sku
        self.operation_type = operation_type  # IN/OUT/ADJUST
        self.quantity = quantity
        self.operator = operator
        self.timestamp = datetime.now()
        self.id = int(time.time() * 1000)

    def __str__(self):
        sign = "+" if self.operation_type == "IN" else "-"
        return (f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{self.operator} {self.operation_type} {self.sku}: "
                f"{sign}{abs(self.quantity)}")


class InventorySystem:
    """库存管理系统"""

    def __init__(self, cache_capacity: int = 100):
        # 主库存数据（哈希表）
        self.inventory: Dict[str, InventoryItem] = {}
        self.inventory_lock = threading.Lock()

        # LRU缓存
        self.cache = LRUCache(cache_capacity)

        # 操作历史记录
        self.operation_history = OrderedDict()
        self.history_lock = threading.Lock()

        # 预警列表
        self.warnings = []
        self.warning_lock = threading.Lock()

    def add_product(self, sku: str, name: str, quantity: int,
                    warning_threshold: int = 10, price: float = 0.0):
        """添加新产品"""
        with self.inventory_lock:
            if sku in self.inventory:
                raise ValueError(f"商品 {sku} 已存在")

            item = InventoryItem(sku, name, quantity, warning_threshold, price)
            self.inventory[sku] = item

            # 添加到缓存
            self.cache.put(sku, item)

            # 记录操作
            self._add_operation(sku, "ADD", quantity, "System")

            # 检查预警
            self._check_warning(item)

            return item

    def get_product(self, sku: str) -> Optional[InventoryItem]:
        """获取商品信息（使用缓存）"""
        # 先尝试从缓存获取
        cached = self.cache.get(sku)
        if cached:
            return cached

        # 缓存未命中，从主存储获取
        with self.inventory_lock:
            if sku not in self.inventory:
                return None

            item = self.inventory[sku]
            # 放入缓存
            self.cache.put(sku, item)
            return item

    def update_stock(self, sku: str, delta: int,
                     operation_type: str = "ADJUST", operator: str = "System"):
        """更新库存"""
        with self.inventory_lock:
            if sku not in self.inventory:
                raise ValueError(f"商品 {sku} 不存在")

            item = self.inventory[sku]
            old_quantity = item.quantity
            item.update_quantity(delta)

            # 更新缓存
            self.cache.put(sku, item)

            # 记录操作
            self._add_operation(sku, operation_type, delta, operator)

            # 检查预警状态变化
            old_warning = old_quantity <= item.warning_threshold
            new_warning = item.check_warning()

            if not old_warning and new_warning:
                self._add_warning(f"商品 {sku} ({item.name}) 库存低于预警阈值")
            elif old_warning and not new_warning:
                self._remove_warning(sku)

            return item

    def inbound(self, sku: str, quantity: int, operator: str = "System"):
        """商品入库"""
        if quantity <= 0:
            raise ValueError("入库数量必须大于0")
        return self.update_stock(sku, quantity, "IN", operator)

    def outbound(self, sku: str, quantity: int, operator: str = "System"):
        """商品出库"""
        if quantity <= 0:
            raise ValueError("出库数量必须大于0")

        item = self.get_product(sku)
        if not item:
            raise ValueError(f"商品 {sku} 不存在")

        if item.quantity < quantity:
            raise ValueError(f"库存不足，当前库存: {item.quantity}")

        return self.update_stock(sku, -quantity, "OUT", operator)

    def _add_operation(self, sku: str, op_type: str, quantity: int, operator: str):
        """添加操作记录"""
        with self.history_lock:
            operation = InventoryOperation(sku, op_type, quantity, operator)
            self.operation_history[operation.id] = operation

            # 保持最多1000条历史记录
            if len(self.operation_history) > 1000:
                self.operation_history.popitem(last=False)

    def _add_warning(self, message: str):
        """添加预警"""
        with self.warning_lock:
            self.warnings.append({
                'message': message,
                'timestamp': datetime.now()
            })

            # 保持最多100条预警
            if len(self.warnings) > 100:
                self.warnings.pop(0)

    def _remove_warning(self, sku: str):
        """移除预警"""
        with self.warning_lock:
            self.warnings = [w for w in self.warnings if sku not in w['message']]

    def _check_warning(self, item: InventoryItem):
        """检查预警"""
        if item.check_warning():
            self._add_warning(f"商品 {item.sku} ({item.name}) 库存低于预警阈值")

    def get_warnings(self):
        """获取预警列表"""
        with self.warning_lock:
            return self.warnings.copy()

    def get_operations(self, limit: int = 10):
        """获取操作记录"""
        with self.history_lock:
            ops = list(self.operation_history.values())[-limit:]
            return ops[::-1]  # 最新的在前

    def get_cache_info(self):
        """获取缓存信息"""
        return self.cache.get_cache_info()

    def get_top_cached_items(self, count: int = 10):
        """获取最热门的缓存商品"""
        return self.cache.get_top_items(count)

    def get_inventory_summary(self):
        """获取库存摘要"""
        with self.inventory_lock:
            total_items = len(self.inventory)
            total_quantity = sum(item.quantity for item in self.inventory.values())
            warning_count = sum(1 for item in self.inventory.values()
                                if item.check_warning())

            return {
                'total_products': total_items,
                'total_quantity': total_quantity,
                'warning_count': warning_count,
                'cache_hit_rate': self.cache.get_hit_rate()
            }


def main():
    """主程序"""
    system = InventorySystem(cache_capacity=50)

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
        system.add_product(sku, name, qty, threshold, price)
        print(f"添加商品: {name} (SKU: {sku}) 库存: {qty}")

    # 模拟一些访问
    print("\n模拟用户访问热门商品...")
    for _ in range(100):
        system.get_product("PROD001")  # iPhone 15 - 热门商品
        system.get_product("PROD003")  # AirPods Pro - 热门商品

    for _ in range(50):
        system.get_product("PROD002")  # MacBook Pro

    # 用户交互
    while True:
        print("\n" + "=" * 50)
        print("电商库存管理系统")
        print("=" * 50)
        print("1. 查询商品库存")
        print("2. 商品入库")
        print("3. 商品出库")
        print("4. 查看LRU缓存状态")
        print("5. 查看库存预警")
        print("6. 查看缓存命中率")
        print("7. 查看操作历史")
        print("8. 查看库存摘要")
        print("9. 添加新商品")
        print("10. 退出系统")

        choice = input("请选择操作 (1-10): ").strip()

        if choice == '1':
            sku = input("请输入商品SKU: ").strip()
            item = system.get_product(sku)
            if item:
                print(f"\n商品详情:")
                print(f"  SKU: {item.sku}")
                print(f"  名称: {item.name}")
                print(f"  当前库存: {item.quantity}")
                print(f"  预警阈值: {item.warning_threshold}")
                print(f"  单价: ¥{item.price:.2f}")
                print(f"  状态: {'⚠️ 需要补货' if item.check_warning() else '✓ 正常'}")
                print(f"  最后更新: {item.updated_at.strftime('%Y-%m-%d %H:%M')}")
            else:
                print("商品不存在")

        elif choice == '2':
            sku = input("请输入商品SKU: ").strip()
            try:
                quantity = int(input("请输入入库数量: ").strip())
                operator = input("请输入操作员(可选): ").strip() or "System"
                item = system.inbound(sku, quantity, operator)
                print(f"入库成功! {item.name} 新库存: {item.quantity}")
            except ValueError as e:
                print(f"操作失败: {e}")
            except Exception as e:
                print(f"发生错误: {e}")

        elif choice == '3':
            sku = input("请输入商品SKU: ").strip()
            try:
                quantity = int(input("请输入出库数量: ").strip())
                operator = input("请输入操作员(可选): ").strip() or "System"
                item = system.outbound(sku, quantity, operator)
                print(f"出库成功! {item.name} 新库存: {item.quantity}")
            except ValueError as e:
                print(f"操作失败: {e}")
            except Exception as e:
                print(f"发生错误: {e}")

        elif choice == '4':
            cache_info = system.get_cache_info()
            print("\nLRU缓存状态:")
            for key, value in cache_info.items():
                print(f"  {key}: {value}")

            top_items = system.get_top_cached_items(5)
            if top_items:
                print("\n最热门商品:")
                for i, (sku, item, count) in enumerate(top_items, 1):
                    print(f"  {i}. {item.name} (SKU: {sku}) - 访问次数: {count}")

        elif choice == '5':
            warnings = system.get_warnings()
            if warnings:
                print("\n库存预警:")
                for warning in warnings[-10:]:  # 显示最近10条
                    timestamp = warning['timestamp'].strftime('%Y-%m-%d %H:%M')
                    print(f"  [{timestamp}] {warning['message']}")
            else:
                print("暂无预警信息")

        elif choice == '6':
            hit_rate = system.cache.get_hit_rate()
            print(f"\n缓存命中率: {hit_rate:.1f}%")
            print(f"缓存命中: {system.cache.hits} 次")
            print(f"缓存未命中: {system.cache.misses} 次")

        elif choice == '7':
            operations = system.get_operations(10)
            if operations:
                print("\n最近操作记录:")
                for op in operations:
                    print(f"  {op}")
            else:
                print("暂无操作记录")

        elif choice == '8':
            summary = system.get_inventory_summary()
            print("\n库存摘要:")
            for key, value in summary.items():
                print(f"  {key}: {value}")

        elif choice == '9':
            sku = input("请输入商品SKU: ").strip()
            name = input("请输入商品名称: ").strip()
            try:
                quantity = int(input("请输入初始库存: ").strip())
                threshold = int(input("请输入预警阈值: ").strip())
                price = float(input("请输入单价: ").strip())

                item = system.add_product(sku, name, quantity, threshold, price)
                print(f"添加成功! {item.name} (SKU: {sku})")
            except ValueError as e:
                print(f"输入错误: {e}")
            except Exception as e:
                print(f"添加失败: {e}")

        elif choice == '10':
            print("正在退出系统...")
            break

        else:
            print("无效选择，请重新输入!")


if __name__ == "__main__":
    main()
