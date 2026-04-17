from src.category import Category
from src.product import Product


def setup_function() -> None:
    """Сбрасывает счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_product_init() -> None:
    """Проверяет корректную инициализацию продукта."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)

    assert product.name == "iPhone 15"
    assert product.description == "256GB, Gray color"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_category_init() -> None:
    """Проверяет корректную инициализацию категории."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product])

    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert category.products == [product]


def test_category_count() -> None:
    """Проверяет подсчет количества категорий."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)

    Category("Смартфоны", "Описание категории", [product])
    Category("Телевизоры", "Описание категории", [product])

    assert Category.category_count == 2


def test_product_count() -> None:
    """Проверяет подсчет количества продуктов."""
    product_1 = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    product_2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    Category("Смартфоны", "Описание категории", [product_1, product_2])

    assert Category.product_count == 2
