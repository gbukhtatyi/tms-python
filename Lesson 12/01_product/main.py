from abc import ABC, abstractmethod
from dataclasses import dataclass


# Задание 1

@dataclass
class Product:
    id: int
    name: str
    price: float


simple_product = Product(1, "Простой продукт", 10)

print("Задание 1")
print("Тип продукта simple_product:", type(simple_product))
print(simple_product)


# Задание 2

@dataclass
class Pizza(Product):
    filling: list[str]
    is_hot: bool
    diameter: int


@dataclass
class Coffee(Product):
    volume: int


pizza = Pizza(2, "Пицца", 100, ['Пеперони', 'Сыр'], False, 30)
cofee100 = Coffee(3, "Кофе 100ml", 10, 100)
cofee200 = Coffee(4, "Кофе 200ml", 20, 200)
cofee300 = Coffee(5, "Кофе 300ml", 30, 300)

for product in pizza, cofee100, cofee200, cofee300:
    print("Тип продукта:", type(product))
    print(product)


# Задание 3


class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        """
        Добавление нового товара
        """

    @abstractmethod
    def sell_product(self, product: Product):
        """
        Продажа
        """

    def all_products(self) -> list[Product]:
        """
        перечень всех продуктов
        """


# Задание 4

class NonProductError(Exception):
    pass


class RealShop(AbstractShop):
    def __init__(self):
        self.products = []
        self.sells = {}

    def add_product(self, product: Product):
        self._validate_product(product)

        if not self._exist_product(product):
            self.products.append(product)

    def sell_product(self, product: Product):
        self._validate_product(product)

        self.sells[product.id] = self.sells.get(product.id, 0) + 1

    def all_products(self) -> list[Product]:
        return self.products

    def _validate_product(self, product: Product):
        if not isinstance(product, Product):
            raise NonProductError("the product parameter must be instance of Product")
        pass

    def _exist_product(self, product: Product):
        for item in self.products:
            if item.id == product.id:
                return True
        else:
            return False


real_shop = RealShop()

real_shop.add_product(cofee100)
real_shop.add_product(cofee200)
real_shop.add_product(cofee300)

real_shop.sell_product(cofee200)
real_shop.sell_product(cofee200)
real_shop.sell_product(cofee300)

print(real_shop.all_products())
print(real_shop.sells)


# Задание 5
# real_shop.add_product(1)
# real_shop.sell_product(1)


# Задание 6

class Furniture(Product):
    pass


class Table(Furniture):
    pass


class Chair(Furniture):
    pass


class Cupboard(Furniture):
    pass


class FurnitureShop(RealShop):
    def _validate_product(self, product: Furniture):
        if not isinstance(product, Furniture):
            raise NonProductError("the product parameter must be instance of Furniture")
        pass


table = Table(10, "Стол", 2000)
chair = Chair(11, "Стул", 1000)
cupboard = Cupboard(12, "Шкаф", 3000)

furniture_shop = FurnitureShop()

furniture_shop.add_product(table)
furniture_shop.add_product(chair)
furniture_shop.add_product(cupboard)

furniture_shop.sell_product(chair)
furniture_shop.sell_product(chair)
furniture_shop.sell_product(table)

print(furniture_shop.all_products())
print(furniture_shop.sells)

# Задание 7
# furniture_shop.sell_product(cofee200)
