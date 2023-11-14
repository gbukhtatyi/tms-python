from .base import Product, RealShop, NonProductError


class FurnitureShopItem(Product):
    pass


class Table(FurnitureShopItem):
    pass


class Chair(FurnitureShopItem):
    pass


class Cupboard(FurnitureShopItem):
    pass


class FurnitureShop(RealShop):
    def _validate_product(self, product: FurnitureShopItem):
        if not isinstance(product, FurnitureShopItem):
            raise NonProductError("the product parameter must be instance of FurnitureShopItem")
        pass
