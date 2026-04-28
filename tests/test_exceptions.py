import pytest
from src.product import Product
from src.category import Category


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