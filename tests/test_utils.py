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
    assert len(categories[0].products) == 3

    assert categories[1].name == "Телевизоры"
    assert len(categories[1].products) == 1
