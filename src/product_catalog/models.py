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
        __price (float): Приватная цена товара.
        quantity (int): Количество в наличии.
    """

    products_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = int(quantity)
        Product.products_count += 1

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создаёт объект Product из словаря с параметрами.

        Аргументы:
            data (dict): Словарь с ключами name, description, price, quantity.

        Возвращает:
            Product: Новый объект товара.
        """
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для приватного атрибута цены.

        Проверяет, что цена не нулевая и не отрицательная.

        Аргументы:
            value (float): Новое значение цены.

        Исключения:
            ValueError: Если цена <= 0.
        """
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля")
        self.__price = float(value)

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, description={self.description!r}, "
            f"price={self.__price}, quantity={self.quantity})"
        )


class Category:
    """
    Класс Category описывает категорию товаров.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        __products (List[Product]): Приватный список товаров категории.
    """

    categories_count: int = 0
    products_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = list(products) if products else []
        Category.categories_count += 1
        self.products_count = len(self.__products)
        Category.products_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.

        Аргументы:
            product (Product): Объект товара для добавления.
        """
        self.__products.append(product)
        self.products_count += 1
        Category.products_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает список товаров категории в виде строки.

        Формат строки:
            Название продукта, 80 руб. Остаток: 15 шт.
        """
        return "\n".join(
            f"{product.name}, {product.price:g} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __repr__(self) -> str:
        return (
            f"Category(name={self.name!r}, description={self.description!r}, "
            f"products={self.__products!r})"
        )