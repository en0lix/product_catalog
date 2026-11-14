# Product Catalog

Каталог товаров с классами `Product` и `Category`.

## 📋 Описание

Проект содержит два класса:

- **Product** — описывает товар (название, описание, цена, количество)
- **Category** — описывает категорию товаров (название, описание, список товаров)

## 🚀 Установка

```bash
pip install -e ".[dev]"

## Функциональность

- `BaseProduct` — абстрактный класс, родитель всех продуктов.
- `ReprMixin` — миксин, печатает `repr` объекта при создании.
- `Product(BaseProduct, ReprMixin)` — базовый товар. При `quantity <= 0` выбрасывает `ValueError`.
- `Smartphone(Product)`, `LawnGrass(Product)` — наследники.
- `Category` — категория с приватным списком и методом `average_price()`.
- `Category.average_price()` — средний ценник; для пустой категории возвращает 0.
- `CategoryIterator` — перебор товаров категории.

## Покрытие тестами
