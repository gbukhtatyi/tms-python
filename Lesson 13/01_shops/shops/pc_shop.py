from .base import Product, BaseShop
from .exceptions import NonProductError


class PcShopItem(Product):
    pass


class VideoCard(PcShopItem):
    pass


class Memory(PcShopItem):
    pass


class HardDisk(PcShopItem):
    pass


class PcShop(BaseShop):
    def _validate_product(self, product: PcShopItem):
        if not isinstance(product, PcShopItem):
            raise NonProductError("the product parameter must be instance of PcShopItem")
        pass
