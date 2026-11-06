"""
Модуль models содержит классы Product, Category и CategoryIterator.
"""

from typing import Iterator, List


class Product:
    """
    Класс Product описывает товар.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        __price (float): Приватный атрибут цены товара.
        quantity (int): Количество в наличии.
    """

    products_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = int(quantity)
        Product.products_count += 1

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для приватного атрибута цены."""
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self.__price = float(value)

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

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {self.__price:g} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """
        Сложение двух товаров: сумма произведений цены на количество.

        Пример: 100×10 + 200×2 = 1400.
        """
        if not isinstance(other, Product):
            raise TypeError(
                f"Нельзя сложить Product с {type(other).__name__}"
            )
        return self.__price * self.quantity + other.__price * other.quantity

    def __repr__(self) -> str:
        return (
            f"Product(name={self.name!r}, description={self.description!r}, "
            f"price={self.__price}, quantity={self.quantity})"
        )


class CategoryIterator:
    """
    Итератор для перебора товаров категории.

    Принимает объект Category и по одному возвращает товары из её списка.
    """

    def __init__(self, category: "Category") -> None:
        self._category = category
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        products = self._category._Category__products
        if self._index >= len(products):
            raise StopIteration
        product = products[self._index]
        self._index += 1
        return product


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
        Category.products_count += 1

    @property
    def products(self) -> str:
        """
        Возвращает список товаров категории в виде строки.

        Формат строки:
            Название продукта, 80 руб. Остаток: 15 шт.
        """
        return "\n".join(str(product) for product in self.__products)

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> CategoryIterator:
        """Позволяет перебирать товары категории в цикле for."""
        return CategoryIterator(self)

    def __repr__(self) -> str:
        return (
            f"Category(name={self.name!r}, description={self.description!r}, "
            f"products={self.__products!r})"
        )