from abc import ABC, abstractmethod
from dataclasses import dataclass


class NonProductError(Exception):
    pass


@dataclass
class Product:
    id: int
    name: str
    price: float


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
