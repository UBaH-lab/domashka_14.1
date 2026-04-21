from src.category import Category
from src.utils import load_data_from_json


def setup_function() -> None:
    """Сбрасывает счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_load_data_from_json() -> None:
    """Проверяет загрузку категорий и продуктов из JSON-файла."""
    categories = load_data_from_json("data/products.json")

    assert len(categories) == 2

    assert categories[0].name == "Смартфоны"
    # products теперь строка, проверяем что в ней есть товары
    assert "Samsung Galaxy C23 Ultra" in categories[0].products  # C23, не S23
    assert "Iphone 15" in categories[0].products
    assert "Xiaomi Redmi Note 11" in categories[0].products

    assert categories[1].name == "Телевизоры"
    assert "55\" QLED 4K" in categories[1].products


def test_load_data_category_count() -> None:
    """Проверяет счетчик категорий после загрузки."""
    load_data_from_json("data/products.json")
    assert Category.category_count == 2


def test_load_data_product_count() -> None:
    """Проверяет счетчик продуктов после загрузки."""
    load_data_from_json("data/products.json")
    assert Category.product_count == 4
