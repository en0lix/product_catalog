"""
Тесты для классов Product и Category.
"""

import pytest

from src.product_catalog.models import Category, Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation(self) -> None:
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        assert product.name == "iPhone"
        assert product.description == "Смартфон Apple"
        assert product.price == 99999.99
        assert product.quantity == 10

    def test_price_getter(self) -> None:
        """Геттер возвращает значение приватного атрибута цены."""
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        assert product.price == 99999.99

    def test_price_setter_valid(self) -> None:
        """Сеттер устанавливает положительную цену."""
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        product.price = 50000
        assert product.price == 50000.0

    def test_price_setter_zero_raises(self) -> None:
        """Сеттер не принимает нулевую цену."""
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        with pytest.raises(ValueError):
            product.price = 0

    def test_price_setter_negative_raises(self) -> None:
        """Сеттер не принимает отрицательную цену."""
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        with pytest.raises(ValueError):
            product.price = -100

    def test_price_is_private(self) -> None:
        """Прямой доступ к __price извне невозможен."""
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        with pytest.raises(AttributeError):
            _ = product.__price

    def test_new_product(self) -> None:
        """Класс-метод new_product создаёт объект из словаря."""
        data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 89999.99,
            "quantity": 3,
        }
        product = Product.new_product(data)
        assert isinstance(product, Product)
        assert product.name == "Ноутбук"
        assert product.description == "Игровой ноутбук"
        assert product.price == 89999.99
        assert product.quantity == 3


class TestCategory:
    """Тесты для класса Category."""

    def test_category_creation(self) -> None:
        products = [
            Product("iPhone", "Смартфон", 99999.99, 10),
            Product("Samsung", "Смартфон", 79999.99, 5),
        ]
        category = Category("Смартфоны", "Мобильные телефоны", products)
        assert category.products_count == 2
        assert isinstance(category.products, str)
        assert "iPhone, 99999.99 руб. Остаток: 10 шт." in category.products
        assert "Samsung, 79999.99 руб. Остаток: 5 шт." in category.products

    def test_add_product(self) -> None:
        """Метод add_product добавляет товар в приватный список."""
        category = Category("Аксессуары", "Компьютерные аксессуары", [])
        mouse = Product("Мышь", "Компьютерная мышь", 80, 15)
        category.add_product(mouse)
        assert "Мышь, 80 руб. Остаток: 15 шт." in category.products

    def test_products_is_private(self) -> None:
        """Прямой доступ к __products извне невозможен."""
        category = Category("Аксессуары", "Описание", [])
        with pytest.raises(AttributeError):
            _ = category.__products