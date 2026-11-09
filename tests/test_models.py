"""
Тесты для классов Product, Smartphone, LawnGrass и Category.
"""

import pytest

from src.product_catalog.models import (
    Category,
    CategoryIterator,
    LawnGrass,
    Product,
    Smartphone,
)


class TestProduct:
    def test_product_creation(self) -> None:
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        assert product.name == "iPhone"
        assert product.price == 99999.99
        assert product.quantity == 10

    def test_product_str(self) -> None:
        product = Product("Мышь", "Компьютерная мышь", 80, 15)
        assert str(product) == "Мышь, 80 руб. Остаток: 15 шт."

    def test_product_add_same_class(self) -> None:
        a = Product("A", "Товар A", 100, 10)
        b = Product("B", "Товар B", 200, 2)
        assert a + b == 1400

    def test_product_add_different_class(self) -> None:
        a = Product("A", "Товар A", 100, 10)
        b = Smartphone("B", "Смартфон", 200, 2, 3.5, "X", 128, "black")
        with pytest.raises(TypeError):
            _ = a + b

    def test_price_setter(self) -> None:
        product = Product("A", "Товар", 100, 1)
        product.price = 200
        assert product.price == 200
        with pytest.raises(ValueError):
            product.price = 0

    def test_new_product(self) -> None:
        data = {"name": "Ноутбук", "description": "Игровой",
                "price": 89999.99, "quantity": 3}
        product = Product.new_product(data)
        assert product.name == "Ноутбук"


class TestSmartphone:
    def test_creation(self) -> None:
        phone = Smartphone(
            "iPhone 15", "Смартфон", 99999.99, 10,
            efficiency=3.5, model="15 Pro", memory=256, color="black",
        )
        assert phone.efficiency == 3.5
        assert phone.model == "15 Pro"
        assert phone.memory == 256
        assert phone.color == "black"

    def test_add_same_class(self) -> None:
        a = Smartphone("A", "A", 100, 2, 1.0, "A", 64, "red")
        b = Smartphone("B", "B", 200, 3, 1.0, "B", 128, "blue")
        assert a + b == 100 * 2 + 200 * 3

    def test_add_different_class(self) -> None:
        phone = Smartphone("A", "A", 100, 1, 1.0, "A", 64, "red")
        grass = LawnGrass("B", "B", 200, 1, "RU", "5 дней", "green")
        with pytest.raises(TypeError):
            _ = phone + grass


class TestLawnGrass:
    def test_creation(self) -> None:
        grass = LawnGrass(
            "Газон", "Трава", 500, 20,
            country="Россия", germination_period="7 дней", color="green",
        )
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "green"


class TestCategory:
    def test_category_creation(self) -> None:
        products = [
            Product("iPhone", "Смартфон", 99999.99, 10),
            Product("Samsung", "Смартфон", 79999.99, 5),
        ]
        category = Category("Смартфоны", "Мобильные телефоны", products)
        assert len(list(category)) == 2

    def test_category_str(self) -> None:
        products = [
            Product("iPhone", "Смартфон", 99999.99, 10),
            Product("Samsung", "Смартфон", 79999.99, 5),
        ]
        category = Category("Смартфоны", "Мобильные телефоны", products)
        assert str(category) == "Смартфоны, количество продуктов: 15 шт."

    def test_add_product_valid(self) -> None:
        category = Category("Аксессуары", "Аксессуары", [])
        product = Product("Мышь", "Мышь", 80, 15)
        category.add_product(product)
        assert "Мышь, 80 руб. Остаток: 15 шт." in category.products

    def test_add_product_invalid(self) -> None:
        category = Category("Аксессуары", "Аксессуары", [])
        with pytest.raises(TypeError):
            category.add_product("не продукт")
        with pytest.raises(TypeError):
            category.add_product(42)

    def test_add_smartphone(self) -> None:
        category = Category("Смартфоны", "Смартфоны", [])
        phone = Smartphone("A", "A", 100, 1, 1.0, "A", 64, "red")
        category.add_product(phone)
        assert len(list(category)) == 1

    def test_category_iterator(self) -> None:
        products = [
            Product("A", "Товар A", 100, 1),
            Product("B", "Товар B", 200, 2),
        ]
        category = Category("Тест", "Описание", products)
        names = [product.name for product in category]
        assert names == ["A", "B"]

    def test_iterator_direct(self) -> None:
        product = Product("A", "Товар A", 100, 1)
        category = Category("Тест", "Описание", [product])
        iterator = CategoryIterator(category)
        assert next(iterator) is product
        with pytest.raises(StopIteration):
            next(iterator)