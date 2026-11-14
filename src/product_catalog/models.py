"""
Модуль models содержит классы BaseProduct, ReprMixin, Product,
Smartphone, LawnGrass, Category и CategoryIterator.
"""

from abc import ABC, abstractmethod
from typing import Iterator, List


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.

    Определяет общую функциональность, которая должна быть у каждого продукта.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = int(quantity)

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление продукта."""
        ...

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение продуктов."""
        ...


class ReprMixin:
    """
    Миксин, который при создании объекта печатает в консоль
    информацию о том, от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(repr(self))


class Product(BaseProduct, ReprMixin):
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
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity)
        Product.products_count += 1

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для приватного атрибута цены."""
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = float(value)

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """Создаёт объект Product из словаря с параметрами."""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    def __str__(self) -> str:
        """Строковое представление товара."""
        return f"{self.name}, {self._price:g} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение двух товаров одного класса."""
        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя сложить {type(self).__name__} с {type(other).__name__}"
            )
        return self._price * self.quantity + other._price * other.quantity

    def __repr__(self) -> str:
        return (
            f"Product('{self.name}', '{self.description}', "
            f"{self._price}, {self.quantity})"
        )


class Smartphone(Product):
    """
    Класс Smartphone — смартфон.

    Дополнительные атрибуты:
        efficiency (float): Производительность.
        model (str): Модель.
        memory (int): Объём встроенной памяти (ГБ).
        color (str): Цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self) -> str:
        return (
            f"Smartphone('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity}, "
            f"{self.efficiency!r}, '{self.model}', {self.memory}, '{self.color}')"
        )


class LawnGrass(Product):
    """
    Класс LawnGrass — трава газонная.

    Дополнительные атрибуты:
        country (str): Страна-производитель.
        germination_period (str): Срок прорастания.
        color (str): Цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self) -> str:
        return (
            f"LawnGrass('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity}, "
            f"'{self.country}', '{self.germination_period}', '{self.color}')"
        )


class CategoryIterator:
    """Итератор для перебора товаров категории."""

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
        self.__products = []
        for product in products:
            self.add_product(product)
        Category.categories_count += 1

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию. Только Product или его наследники."""
        if not isinstance(product, Product):
            raise TypeError(
                f"В категорию можно добавлять только Product и его наследников, "
                f"а не {type(product).__name__}"
            )
        self.__products.append(product)
        Category.products_count += 1

    @property
    def products(self) -> str:
        """Список товаров категории в виде строки."""
        return "\n".join(str(product) for product in self.__products)

    def average_price(self) -> float:
        """
        Средний ценник всех товаров категории.

        Складывает только цены (self.price) всех товаров
        и делит на количество товаров в категории.
        Если товаров нет — возвращает 0.
        """
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0

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