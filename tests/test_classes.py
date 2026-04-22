import pytest
from src.category import Category
from src.product import Product


def setup_function() -> None:
    """Сбрасывает счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


# ========== Тесты Product ==========


def test_product_init() -> None:
    """Проверяет инициализацию продукта."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000
    assert product.quantity == 10


def test_product_new_product() -> None:
    """Проверяет создание продукта из словаря."""
    data = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 100000,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 100000
    assert product.quantity == 5


def test_product_price_getter() -> None:
    """Проверяет геттер цены."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    assert product.price == 50000


def test_product_price_setter_positive() -> None:
    """Проверяет сеттер цены с положительным значением."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    product.price = 60000
    assert product.price == 60000


def test_product_price_setter_negative(capsys) -> None:
    """Проверяет сеттер цены с отрицательным значением."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    product.price = -100
    assert product.price == 50000  # цена не изменилась
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_setter_zero(capsys) -> None:
    """Проверяет сеттер цены с нулевым значением."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    product.price = 0
    assert product.price == 50000  # цена не изменилась
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str() -> None:
    """Проверяет строковое представление продукта."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    assert str(product) == "Телефон, 50000 руб. Остаток: 10 шт."


def test_product_add() -> None:
    """Проверяет сложение продуктов."""
    product1 = Product("Телефон", "Смартфон", 100, 10)
    product2 = Product("Планшет", "iPad", 200, 2)
    result = product1 + product2
    assert result == 1400.0


def test_product_add_same_products() -> None:
    """Проверяет сложение одинаковых продуктов."""
    product1 = Product("Телефон", "Смартфон", 5000, 3)
    product2 = Product("Телефон", "Смартфон", 5000, 3)
    result = product1 + product2
    assert result == 30000.0


# ========== Тесты Category ==========


def test_category_init() -> None:
    """Проверяет инициализацию категории."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    category = Category("Гаджеты", "Электроника", [product])
    assert category.name == "Гаджеты"
    assert category.description == "Электроника"
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_add_product() -> None:
    """Проверяет добавление продукта в категорию."""
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    category = Category("Гаджеты", "Электроника", [product1])
    product2 = Product("Планшет", "iPad", 80000, 5)
    category.add_product(product2)
    assert Category.product_count == 2


def test_category_products_getter() -> None:
    """Проверяет геттер products категории."""
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    product2 = Product("Планшет", "iPad", 80000, 5)
    category = Category("Гаджеты", "Электроника", [product1, product2])
    result = category.products
    assert "Телефон, 50000 руб. Остаток: 10 шт." in result
    assert "Планшет, 80000 руб. Остаток: 5 шт." in result


def test_category_str() -> None:
    """Проверяет строковое представление категории."""
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    product2 = Product("Планшет", "iPad", 80000, 5)
    category = Category("Гаджеты", "Электроника", [product1, product2])
    assert str(category) == "Гаджеты, количество продуктов: 15 шт."


def test_category_str_empty() -> None:
    """Проверяет строковое представление пустой категории."""
    category = Category("Пустая", "Нет товаров", [])
    assert str(category) == "Пустая, количество продуктов: 0 шт."


# ========== Тесты CategoryIterator (дополнительное задание) ==========


def test_category_iterator() -> None:
    """Проверяет итератор категории."""
    product1 = Product("Телефон", "Смартфон", 50000, 10)
    product2 = Product("Планшет", "iPad", 80000, 5)
    product3 = Product("Часы", "Smart Watch", 30000, 20)
    category = Category("Гаджеты", "Электроника", [product1, product2, product3])

    products_list = []
    for product in category:
        products_list.append(product)

    assert len(products_list) == 3
    assert products_list[0] == product1
    assert products_list[1] == product2
    assert products_list[2] == product3


def test_category_iterator_stop_iteration() -> None:
    """Проверяет, что итератор вызывает StopIteration в конце."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    category = Category("Гаджеты", "Электроника", [product])

    iterator = iter(category)
    next(iterator)  # получаем первый продукт

    # Больше продуктов нет — должно вызвать StopIteration
    with pytest.raises(StopIteration):
        next(iterator)
