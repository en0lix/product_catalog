"""
Тесты для классов Product и Category.
"""

from src.product_catalog.models import Category, Product


class TestProduct:
    """Тесты для класса Product."""

    def test_product_creation(self) -> None:
        product = Product("iPhone", "Смартфон Apple", 99999.99, 10)
        assert product.name == "iPhone"
        assert product.description == "Смартфон Apple"
        assert product.price == 99999.99
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category."""

    def test_category_creation(self) -> None:
        products = [
            Product("iPhone", "Смартфон", 99999.99, 10),
            Product("Samsung", "Смартфон", 79999.99, 5),
        ]
        category = Category("Смартфоны", "Мобильные телефоны", products)
        assert len(category.products) == 2
        assert category.products_count == 2