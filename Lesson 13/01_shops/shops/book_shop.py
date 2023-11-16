from .base import Product, BaseShop
from .exceptions import NonProductError

class BookShopItem(Product):
    pass


class Book(BookShopItem):
    pass


class Journal(BookShopItem):
    pass


class BookShop(BaseShop):
    def _validate_product(self, product: BookShopItem):
        if not isinstance(product, BookShopItem):
            raise NonProductError("the product parameter must be instance of BookShopItem")
        pass
