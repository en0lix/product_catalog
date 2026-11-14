"""
Тесты для классов Product, Smartphone, LawnGrass и Category.
"""

import pytest

from src.product_catalog.models import (
    BaseProduct,
    Category,
    CategoryIterator,
    LawnGrass,
    Product,
    ReprMixin,
    Smartphone,
)


class TestBaseProduct:
    def test_product_is_baseproduct(self) -> None:
        product = Product("A", "A", 100, 1)
        assert isinstance(product, BaseProduct)

    def test_cannot_instantiate_baseproduct(self) -> None:
        with pytest.raises(TypeError):
            BaseProduct("A", "A", 100, 1)


class TestReprMixin:
    def test_repr_printed_on_create(self, capsys) -> None:
        Product("Продукт1", "Описание продукта", 1200, 10)
        captured = capsys.readouterr()
        assert "Product('Продукт1', 'Описание продукта', 1200.0, 10)" in captured.out


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
        a = Product("A", "A", 100, 10)
        b = Product("B", "B", 200, 2)
        assert a + b == 1400

    def test_product_add_different_class(self) -> None:
        a = Product("A", "A", 100, 10)
        b = Smartphone("B", "B", 200, 2, 3.5, "X", 128, "black")
        with pytest.raises(TypeError):
            _ = a + b

    def test_price_setter(self) -> None:
        product = Product("A", "A", 100, 1)
        product.price = 200
        assert product.price == 200
        with pytest.raises(ValueError):
            product.price = 0

    def test_zero_quantity_raises(self) -> None:
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("A", "A", 100, 0)

    def test_negative_quantity_raises(self) -> None:
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("A", "A", 100, -5)

    def test_new_product(self) -> None:
        data = {"name": "Ноутбук", "description": "Игровой",
                "price": 89999.99, "quantity": 3}
        product = Product.new_product(data)
        assert product.name == "Ноутбук"


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

    def test_add_product_invalid(self) -> None:
        category = Category("Аксессуары", "Аксессуары", [])
        with pytest.raises(TypeError):
            category.add_product("не продукт")

    def test_average_price(self) -> None:
        products = [
            Product("A", "A", 100, 1),
            Product("B", "B", 200, 1),
            Product("C", "C", 300, 1),
        ]
        category = Category("Тест", "Описание", products)
        assert category.average_price() == 200.0

    def test_average_price_empty_category(self) -> None:
        category = Category("Пустая", "Пустая категория", [])
        assert category.average_price() == 0

    def test_average_price_uses_only_price(self) -> None:
        # Проверяем, что складываются только цены, не умножаются на quantity
        products = [
            Product("A", "A", 100, 10),
            Product("B", "B", 200, 5),
        ]
        category = Category("Тест", "Описание", products)
        assert category.average_price() == 150.0

    def test_category_iterator(self) -> None:
        products = [
            Product("A", "A", 100, 1),
            Product("B", "B", 200, 2),
        ]
        category = Category("Тест", "Описание", products)
        names = [product.name for product in category]
        assert names == ["A", "B"]