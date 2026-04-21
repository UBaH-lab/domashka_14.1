import pytest
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


def test_product_price_getter() -> None:
    """Проверяет геттер цены."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    assert product.price == 210000.0


def test_product_price_setter_valid() -> None:
    """Проверяет сеттер цены с корректным значением."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    product.price = 200000.0
    assert product.price == 200000.0


def test_product_price_setter_zero(capsys) -> None:
    """Проверяет сеттер цены при нулевом значении."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    product.price = 0

    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 210000.0


def test_product_price_setter_negative(capsys) -> None:
    """Проверяет сеттер цены при отрицательном значении."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    product.price = -1000.0

    captured = capsys.readouterr()
    assert captured.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 210000.0


def test_product_new_product() -> None:
    """Проверяет класс-метод new_product."""
    product_data = {
        "name": "iPhone 15",
        "description": "256GB, Gray color",
        "price": 210000.0,
        "quantity": 8,
    }
    product = Product.new_product(product_data)

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


def test_category_products_getter() -> None:
    """Проверяет геттер products возвращает строку нужного формата."""
    product = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product])

    expected = "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert category.products == expected


def test_category_products_getter_multiple() -> None:
    """Проверяет геттер products с несколькими товарами."""
    product1 = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    product2 = Product("Samsung Galaxy", "128GB, Black", 150000.0, 5)
    category = Category("Смартфоны", "Описание категории", [product1, product2])

    expected = (
        "iPhone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Samsung Galaxy, 150000.0 руб. Остаток: 5 шт.\n"
    )
    assert category.products == expected


def test_category_add_product() -> None:
    """Проверяет добавление продукта через add_product."""
    product1 = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product1])

    product2 = Product("Samsung Galaxy", "128GB, Black", 150000.0, 5)
    category.add_product(product2)

    # Проверяем, что продукт добавился (через геттер)
    assert "Samsung Galaxy" in category.products
    assert "150000.0 руб." in category.products


def test_category_add_product_counter() -> None:
    """Проверяет, что add_product увеличивает счетчик товаров."""
    product1 = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product1])

    initial_count = Category.product_count

    product2 = Product("Samsung Galaxy", "128GB, Black", 150000.0, 5)
    category.add_product(product2)

    assert Category.product_count == initial_count + 1


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
