import pytest
from src.product import Product
from src.category import Category
from src.exceptions import AddProductError


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Товар", "Описание", 100.0, 0)


def test_product_positive_quantity():
    """Тест создания продукта с положительным количеством."""
    product = Product("Товар", "Описание", 100.0, 10)
    assert product.quantity == 10


def test_get_average_price():
    """Тест подсчёта среднего ценника."""
    product1 = Product("Товар1", "Описание", 100.0, 5)
    product2 = Product("Товар2", "Описание", 200.0, 10)
    category = Category("Категория", "Описание", [product1, product2])

    assert category.get_average_price() == 150.0


def test_get_average_price_empty_category():
    """Тест среднего ценника пустой категории."""
    category = Category("Пустая категория", "Описание", [])

    assert category.get_average_price() == 0.0


# ========== Дополнительные тесты для try/except/else/finally ==========


def test_add_product_zero_quantity_prints_error(capsys):
    """Тест добавления товара с нулевым количеством в категорию."""
    product = Product("Товар", "Описание", 100.0, 1)
    category = Category("Категория", "Описание", [])

    # Меняем количество на 0 после создания (чтобы обойти проверку в __init__)
    product.quantity = 0

    category.add_product(product)

    captured = capsys.readouterr()
    assert "Ошибка: Попытка добавить товар с нулевым количеством" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_add_product_success_prints_message(capsys):
    """Тест успешного добавления товара."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание", [])

    category.add_product(product)

    captured = capsys.readouterr()
    assert "Товар успешно добавлен" in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_add_product_error_increments_product_count():
    """Тест, что при ошибке количество продуктов не увеличивается."""
    product = Product("Товар", "Описание", 100.0, 1)
    category = Category("Категория", "Описание", [])

    initial_count = Category.product_count
    product.quantity = 0

    category.add_product(product)

    assert Category.product_count == initial_count


def test_add_product_success_increments_product_count():
    """Тест, что при успехе количество продуктов увеличивается."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание", [])

    initial_count = Category.product_count

    category.add_product(product)

    assert Category.product_count == initial_count + 1
