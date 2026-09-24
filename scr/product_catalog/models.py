"""
Модуль models содержит классы Product и Category.
"""

from typing import List


class Product:
    """
    Класс Product описывает товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        price (float): Цена товара.
        quantity (int): Количество в наличии.
    """

    products_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)
        Product.products_count += 1

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, description={self.description!r}, "
            f"price={self.price}, quantity={self.quantity})"
        )


class Category:
    """
    Класс Category описывает категорию товаров.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        products (List[Product]): Список товаров категории.
    """

    categories_count: int = 0
    products_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = list(products) if products else []
        Category.categories_count += 1
        self.products_count = len(self.products)
        Category.products_count += len(self.products)

    def __repr__(self) -> str:
        return (
            f"Category(name={self.name!r}, description={self.description!r}, "
            f"products={self.products!r})"
        )