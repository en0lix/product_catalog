"""
Тесты для классов Product и Category.
"""

from scr.product_catalog.models import Category, Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation(self) -> None:
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        assert product.name == "iPhone"
        assert product.description == "Смартфон Apple"
        assert product.price == 99999.99
        assert product.quantity == 10

    def test_new_product(self) -> None:
        data = {
            "name": "Ноутбук",
            "description": "Игровой ноутбук",
            "price": 89999.99,
            "quantity": 3,
        }
        product = Product.new_product(data)
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
        category = Category("Аксессуары", "Компьютерные аксессуары", [])
        product = Product("Мышь", "Компьютерная мышь", 80, 15)
        category.add_product(product)
        assert category.products_count == 1
        assert "Мышь, 80 руб. Остаток: 15 шт." in category.products