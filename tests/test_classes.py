import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


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


def test_product_price_setter_negative(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет сеттер цены с отрицательным значением."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    product.price = -100
    assert product.price == 50000  # цена не изменилась
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_setter_zero(capsys: pytest.CaptureFixture[str]) -> None:
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


# ========== Тесты Smartphone ==========


def test_smartphone_init() -> None:
    """Проверяет инициализацию смартфона."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=5,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )
    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "Флагман Apple"
    assert smartphone.price == 100000
    assert smartphone.quantity == 5
    assert smartphone.efficiency == "A17 Pro"
    assert smartphone.model == "iPhone 15 Pro Max"
    assert smartphone.memory == 256
    assert smartphone.color == "Титановый"


def test_smartphone_str() -> None:
    """Проверяет строковое представление смартфона."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=5,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )
    assert str(smartphone) == "iPhone 15, 100000 руб. Остаток: 5 шт."


def test_smartphone_add() -> None:
    """Проверяет сложение смартфонов."""
    phone1 = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=2,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )
    phone2 = Smartphone(
        name="Samsung S24",
        description="Флагман Samsung",
        price=80000,
        quantity=3,
        efficiency="Snapdragon 8",
        model="Galaxy S24 Ultra",
        memory=512,
        color="Черный",
    )
    result = phone1 + phone2
    assert result == 440000.0


# ========== Тесты LawnGrass ==========


def test_lawn_grass_init() -> None:
    """Проверяет инициализацию травы газонной."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Для дачи",
        price=500,
        quantity=100,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый",
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Для дачи"
    assert grass.price == 500
    assert grass.quantity == 100
    assert grass.country == "Россия"
    assert grass.germination_period == "2 недели"
    assert grass.color == "Зеленый"


def test_lawn_grass_str() -> None:
    """Проверяет строковое представление травы газонной."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Для дачи",
        price=500,
        quantity=100,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый",
    )
    assert str(grass) == "Газонная трава, 500 руб. Остаток: 100 шт."


def test_lawn_grass_add() -> None:
    """Проверяет сложение травы газонной."""
    grass1 = LawnGrass(
        name="Газонная трава",
        description="Для дачи",
        price=500,
        quantity=10,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый",
    )
    grass2 = LawnGrass(
        name="Спортивная трава",
        description="Для стадиона",
        price=800,
        quantity=5,
        country="Германия",
        germination_period="3 недели",
        color="Темно-зеленый",
    )
    result = grass1 + grass2
    assert result == 9000.0


# ========== Тесты ограничения сложения ==========


def test_add_smartphone_and_product() -> None:
    """Проверяет ошибку при сложении смартфона и обычного продукта."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=2,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )
    product = Product("Телефон", "Обычный телефон", 10000, 5)

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = smartphone + product


def test_add_smartphone_and_lawn_grass() -> None:
    """Проверяет ошибку при сложении смартфона и травы газонной."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=2,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )
    grass = LawnGrass(
        name="Газонная трава",
        description="Для дачи",
        price=500,
        quantity=10,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый",
    )

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = smartphone + grass


def test_add_product_and_smartphone() -> None:
    """Проверяет ошибку при сложении обычного продукта и смартфона."""
    product = Product("Телефон", "Обычный телефон", 10000, 5)
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=2,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )

    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        _ = product + smartphone


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


def test_category_add_smartphone() -> None:
    """Проверяет добавление смартфона в категорию."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагман Apple",
        price=100000,
        quantity=5,
        efficiency="A17 Pro",
        model="iPhone 15 Pro Max",
        memory=256,
        color="Титановый",
    )
    category = Category("Смартфоны", "Мобильные устройства", [])
    category.add_product(smartphone)
    assert Category.product_count == 1


def test_category_add_lawn_grass() -> None:
    """Проверяет добавление травы газонной в категорию."""
    grass = LawnGrass(
        name="Газонная трава",
        description="Для дачи",
        price=500,
        quantity=100,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый",
    )
    category = Category("Сад", "Товары для сада", [])
    category.add_product(grass)
    assert Category.product_count == 1


def test_category_add_non_product() -> None:
    """Проверяет ошибку при добавлении не продукта в категорию."""
    category = Category("Гаджеты", "Электроника", [])

    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product("не продукт")


def test_category_add_non_product_number() -> None:
    """Проверяет ошибку при добавлении числа в категорию."""
    category = Category("Гаджеты", "Электроника", [])

    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product(123)


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


# ========== Тесты CategoryIterator ==========


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
    next(iterator)

    with pytest.raises(StopIteration):
        next(iterator)


# ========== Тесты для абстрактного класса BaseProduct ==========

def test_product_is_subclass_of_base_product():
    """Проверяет, что Product наследуется от BaseProduct."""
    from src.base_product import BaseProduct
    from src.product import Product

    assert issubclass(Product, BaseProduct)


def test_smartphone_is_subclass_of_product():
    """Проверяет, что Smartphone наследуется от Product."""
    from src.product import Product, Smartphone

    assert issubclass(Smartphone, Product)


def test_lawn_grass_is_subclass_of_product():
    """Проверяет, что LawnGrass наследуется от Product."""
    from src.product import LawnGrass, Product

    assert issubclass(LawnGrass, Product)


def test_base_product_is_abstract():
    """Проверяет, что BaseProduct - абстрактный класс."""
    from abc import ABC
    from src.base_product import BaseProduct

    assert issubclass(BaseProduct, ABC)


def test_cannot_instantiate_base_product() -> None:
    """Проверяет, что нельзя создать экземпляр абстрактного класса."""
    from src.base_product import BaseProduct

    with pytest.raises(TypeError):
        BaseProduct("Товар", "Описание", 1000.0, 10)  # type: ignore


# ========== Тесты для миксина LogMixin ==========

def test_mixin_prints_on_creation(capsys):
    """Проверяет, что миксин печатает информацию при создании."""
    from src.product import Product

    Product("Товар", "Описание", 1000.0, 5)

    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out
    assert "Товар" in captured.out


def test_mixin_prints_smartphone_creation(capsys):
    """Проверяет, что миксин печатает информацию при создании смартфона."""
    from src.product import Smartphone

    Smartphone(
        "iPhone", "Описание", 100000.0, 3,
        "A15", "15 Pro", 256, "Black"
    )

    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone" in captured.out


def test_mixin_repr():
    """Проверяет, что миксин добавляет метод __repr__."""
    from src.product import Product

    product = Product("Товар", "Описание", 1000.0, 5)
    repr_str = repr(product)

    assert "Product" in repr_str


# ========== Тесты для абстрактного класса BaseUnit ==========

def test_base_unit_is_abstract():
    """Проверяет, что BaseUnit - абстрактный класс."""
    from abc import ABC
    from src.base_unit import BaseUnit

    assert issubclass(BaseUnit, ABC)


def test_cannot_instantiate_base_unit() -> None:
    """Проверяет, что нельзя создать экземпляр абстрактного класса."""
    from src.base_unit import BaseUnit

    with pytest.raises(TypeError):
        BaseUnit("Название", "Описание")  # type: ignore


def test_category_is_subclass_of_base_unit():
    """Проверяет, что Category наследуется от BaseUnit."""
    from src.base_unit import BaseUnit
    from src.category import Category

    assert issubclass(Category, BaseUnit)


def test_order_is_subclass_of_base_unit():
    """Проверяет, что Order наследуется от BaseUnit."""
    from src.base_unit import BaseUnit
    from src.order import Order

    assert issubclass(Order, BaseUnit)


# ========== Тесты для класса Order ==========

def test_order_init():
    """Проверяет создание заказа."""
    from src.order import Order
    from src.product import Product

    product = Product("Телефон", "Смартфон", 50000.0, 10)
    order = Order("Заказ #1", "Тестовый заказ", product, 3)

    assert order.name == "Заказ #1"
    assert order.description == "Тестовый заказ"
    assert order.product == product
    assert order.quantity == 3


def test_order_total_price():
    """Проверяет вычисление итоговой стоимости."""
    from src.order import Order
    from src.product import Product

    product = Product("Телефон", "Смартфон", 50000.0, 10)
    order = Order("Заказ #1", "Тестовый заказ", product, 3)

    assert order.total_price == 150000.0


def test_order_str():
    """Проверяет строковое представление заказа."""
    from src.order import Order
    from src.product import Product

    product = Product("Телефон", "Смартфон", 50000.0, 10)
    order = Order("Заказ #1", "Тестовый заказ", product, 2)

    result = str(order)

    assert "Заказ #1" in result
    assert "Телефон" in result
    assert "2 шт." in result
    assert "100000" in result


def test_order_with_smartphone():
    """Проверяет заказ со смартфоном."""
    from src.order import Order
    from src.product import Smartphone

    smartphone = Smartphone(
        "iPhone 15", "512GB, Gray", 150000.0, 5,
        "A17", "15 Pro Max", 512, "Gray"
    )
    order = Order("Заказ #2", "Заказ смартфона", smartphone, 1)

    assert order.product.name == "iPhone 15"
    assert order.total_price == 150000.0
