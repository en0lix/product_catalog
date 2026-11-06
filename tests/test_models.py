"""
Тесты для классов Product и Category.
"""

import pytest

from src.product_catalog.models import Category, CategoryIterator, Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation(self) -> None:
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        assert product.name == "iPhone"
        assert product.description == "Смартфон Apple"
        assert product.price == 99999.99
        assert product.quantity == 10

    def test_product_str(self) -> None:
        product = Product("Мышь", "Компьютерная мышь", 80, 15)
        assert str(product) == "Мышь, 80 руб. Остаток: 15 шт."

    def test_product_add(self) -> None:
        a = Product("A", "Товар A", 100, 10)
        b = Product("B", "Товар B", 200, 2)
        assert a + b == 1400

    def test_product_add_type_error(self) -> None:
        a = Product("A", "Товар A", 100, 10)
        with pytest.raises(TypeError):
            _ = a + 5

    def test_price_setter_positive(self) -> None:
        product = Product("A", "Товар", 100, 1)
        product.price = 200
        assert product.price == 200

    def test_price_setter_invalid(self) -> None:
        product = Product("A", "Товар", 100, 1)
        with pytest.raises(ValueError):
            product.price = 0

    def test_new_product(self) -> None:
        data = {
            "name": "Ноутбук",
            "description": "Игровой",
            "price": 89999.99,
            "quantity": 3,
        }
        product = Product.new_product(data)
        assert product.name == "Ноутбук"
        assert product.price == 89999.99


class TestCategory:
    """Тесты для класса Category."""

    def test_category_creation(self) -> None:
        products = [
            Product("iPhone", "Смартфон", 99999.99, 10),
            Product("Samsung", "Смартфон", 79999.99, 5),
        ]
        category = Category("Смартфоны", "Мобильные телефоны", products)
        assert category.products_count == 2

    def test_category_str(self) -> None:
        products = [
            Product("iPhone", "Смартфон", 99999.99, 10),
            Product("Samsung", "Смартфон", 79999.99, 5),
        ]
        category = Category("Смартфоны", "Мобильные телефоны", products)
        assert str(category) == "Смартфоны, количество продуктов: 15 шт."

    def test_add_product(self) -> None:
        category = Category("Аксессуары", "Компьютерные аксессуары", [])
        product = Product("Мышь", "Компьютерная мышь", 80, 15)
        category.add_product(product)
        assert "Мышь, 80 руб. Остаток: 15 шт." in category.products

    def test_category_iterator(self) -> None:
        products = [
            Product("A", "Товар A", 100, 1),
            Product("B", "Товар B", 200, 2),
        ]
        category = Category("Тест", "Описание", products)
        names = [product.name for product in category]
        assert names == ["A", "B"]

    def test_category_iterator_direct(self) -> None:
        product = Product("A", "Товар A", 100, 1)
        category = Category("Тест", "Описание", [product])
        iterator = CategoryIterator(category)
        assert next(iterator) is product
        with pytest.raises(StopIteration):
            next(iterator)