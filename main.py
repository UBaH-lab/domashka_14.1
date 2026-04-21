from src.category import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1.products)  # теперь выводит отформатированную строку
    print(Category.category_count)
    print(Category.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        (
            "Современный телевизор, который позволяет "
            "наслаждаться просмотром, станет вашим другом и помощником"
        ),
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Демонстрация новой функциональности
    print("\n--- Новая функциональность ---\n")

    # 1. Добавление товара через add_product()
    new_product = Product("Samsung Galaxy A54", "256GB, Черный", 45000.0, 20)
    category1.add_product(new_product)
    print("Добавлен новый товар в категорию Смартфоны:")
    print(category1.products)
    print(f"Общее количество товаров: {Category.product_count}")

    # 2. Создание товара через класс-метод new_product()
    product_data = {
        "name": "Google Pixel 8",
        "description": "128GB, Черный",
        "price": 85000.0,
        "quantity": 12,
    }
    product5 = Product.new_product(product_data)
    print(f"Создан товар через new_product: {product5.name}, {product5.price} руб.")

    # 3. Работа с сеттером цены
    print("\nИзменение цены товара:")
    print(f"Текущая цена: {product1.price} руб.")

    # Пытаемся установить корректную цену
    product1.price = 170000.0
    print(f"Новая цена после изменения: {product1.price} руб.")

    # Пытаемся установить некорректную цену
    print("\nПопытка установить нулевую цену:")
    product1.price = 0
    print(f"Цена осталась прежней: {product1.price} руб.")

    # Пытаемся установить отрицательную цену
    print("\nПопытка установить отрицательную цену:")
    product1.price = -5000
    print(f"Цена осталась прежней: {product1.price} руб.")