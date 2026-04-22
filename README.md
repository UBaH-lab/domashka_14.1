# PythonProject25

Проект с классами Product и Category.

## Возможности

### Product
- Создание продукта с названием, описанием, ценой и количеством
- Создание продукта из словаря через `new_product()`
- Геттер и сеттер для цены с валидацией
- Магический метод `__str__` — строковое представление продукта
- Магический метод `__add__` — сложение продуктов

### Category
- Создание категории с названием, описанием и списком продуктов
- Подсчёт количества категорий (`category_count`)
- Подсчёт количества продуктов (`product_count`)
- Добавление продуктов в категорию
- Геттер `products` — строковое представление всех продуктов
- Магический метод `__str__` — строковое представление категории
- Итератор для перебора продуктов категории

### Дополнительно
- Загрузка данных из JSON
- Полное тестирование через pytest (99% покрытие)
- Проверка стиля кода через flake8
- Проверка типов через mypy

## Структура проекта

src/ ├── init.py ├── category.py # Класс Category ├── category_iterator.py # Итератор для Category ├── product.py # Класс Product └── utils.py # Утилиты для работы с JSON

tests/ ├── init.py ├── test_classes.py # Тесты Product, Category, CategoryIterator └── test_utils.py # Тесты утилит

main.py # Точка входа



## Установка

```bash
pip install -r requirements.txt
```

Запуск
```bash

python main.py
```

Тестирование

```bash
# Запуск тестов с покрытием
pytest --cov=src --cov-report=term-missing
```

# HTML-отчёт о покрытии
pytest --cov=src --cov-report=html
start htmlcov/index.html
Проверка кода
```bash

# Проверка стиля
flake8 .
# Проверка типов
mypy .
```
Примеры использования
python

from src.product import Product
from src.category import Category

# Создание продуктов
product1 = Product("Телефон", "Смартфон", 50000, 10)
product2 = Product("Планшет", "iPad", 80000, 5)

# Строковое представление
print(product1)  # Телефон, 50000 руб. Остаток: 10 шт.

# Сложение продуктов
total = product1 + product2
print(total)  # 900000.0

# Создание категории
category = Category("Гаджеты", "Электроника", [product1, product2])

# Строковое представление категории
print(category)  # Гаджеты, количество продуктов: 15 шт.

# Итерация по продуктам
for product in category:
    print(product.name)
Технологии
Python 3.13
pytest
pytest-cov
flake8
mypy

