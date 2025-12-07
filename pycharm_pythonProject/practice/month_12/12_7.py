from enum import Enum


class ProductType(Enum):
    """商品类型枚举"""
    PHYSICAL = "实体商品"
    DIGITAL = "数字商品"


class Product:
    def __init__(self, product_id, name, price, inventory):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.inventory = inventory
        self.prd_list = []

    def __str__(self):
        return f"ID:{self.product_id} 名称：{self.name} 价格：{self.price} 库存：{self.inventory}"


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, inventory, infor):
        super().__init__(product_id, name, price, inventory)
        self.infor = infor
        self.type = ProductType.PHYSICAL
    pass


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, inventory, download, file_size):
        super().__init__(product_id, name, price, inventory)
        self.download = download
        self.file_size = file_size
        self.type = ProductType.DIGITAL

    pass


class ShoppingCart:

    pass


class Order:

    pass


if __name__ == '__main__':
    pass
