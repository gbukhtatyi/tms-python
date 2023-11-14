from .base import Product
from dataclasses import dataclass


@dataclass
class Pizza(Product):
    filling: list[str]
    is_hot: bool
    diameter: int


@dataclass
class Coffee(Product):
    volume: int
