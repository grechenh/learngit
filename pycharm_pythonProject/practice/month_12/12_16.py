class Product:
    """商品类"""

    def __init__(self, sku, name, product_type, inventory: int):
        self.sku = sku
        self.name = name
        self.product_type = product_type
        self.inventory = inventory

    def __str__(self):
        """商品 1: P001, iPhone 13, 手机, 50"""
        return f"商品ID：{self.sku},  名称： {self.name}, 类别：{self.product_type},库存： {self.inventory}"


class InventoryManager:
    """库存管理类"""

    def __init__(self):
        """存储方式：{sku：Product}"""
        self.cont_dict = {}

    def add_product(self, sku, name, product_type, inventory):
        """add"""
        self.cont_dict[sku] = Product(sku=sku, name=name, product_type=product_type, inventory=inventory)

    def order_product(self):
        """order"""
        items = list(self.cont_dict.values())
        """冒泡排序"""
        for i in range(len(items) - 1, 0, -1):
            for j in range(i):
                if items[j].inventory > items[j + 1].inventory:
                    items[j], items[j+1] = items[j+1], items[j]
        # items.sort(key=lambda x: x.inventory, reverse=True)
        return [(item.sku, item.name, item.product_type, item.inventory) for item in items]

    def query_product(self):
        """遍历查询O（n）"""
        cont_list = []
        for item in self.cont_dict.values():
            if item.inventory == 0:
                cont_list.append(item)
        return cont_list

    pass


def main():
    item = InventoryManager()
    """
        商品 1: P001, iPhone 13, 手机, 50
        商品 2: P002, MacBook Pro, 电脑, 30
        商品 3: P003, AirPods Pro, 耳机, 100
        商品 4: P004, iPad Air, 平板, 25
    """
    products = [
        ("P001", "iPhone 13", "手机", 50),
        ("P003", "AirPods Pro", "耳机", 100),
        ("P004", "iPad Air", "平板", 25)
    ]
    for sku, name, product_type, inventory in products:
        item.add_product(sku=sku, name=name, product_type=product_type, inventory=inventory)
        print(f"添加商品: {name} (SKU: {sku})      类型：{product_type}      库存: {inventory}")

    ordered_product = item.order_product()
    for sku, name, product_type, inventory in ordered_product:
        print(f"排序后的商品: {name} (SKU: {sku})     类型：{product_type}      库存: {inventory}")

    already_query_product = item.query_product()
    """查询库存为0的商品"""
    if len(already_query_product) == 0:
        print("无")
    else:
        for sku, name, product_type, inventory in already_query_product:
            print(f"库存为0的商品: {name} (SKU: {sku})      类型：{product_type}")

    query_item = item.cont_dict["P001"]
    """字典查询商品"""
    print(query_item)


if __name__ == '__main__':
    main()
