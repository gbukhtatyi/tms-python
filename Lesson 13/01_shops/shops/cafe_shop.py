from dataclasses import dataclass
from .base import Product, BaseShop
from .exceptions import NonProductError


class CafeShopItem(Product):
    pass


@dataclass
class Pizza(CafeShopItem):
    filling: list[str]
    is_hot: bool
    diameter: int


@dataclass
class Coffee(CafeShopItem):
    volume: int


class CafeShop(BaseShop):
    def _validate_product(self, product: CafeShopItem):
        if not isinstance(product, CafeShopItem):
            raise NonProductError("the product parameter must be instance of CafeShopItem")
        pass
