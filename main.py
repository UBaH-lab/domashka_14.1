from src.category import Category
from src.product import Product


product_1 = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
product_2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
product_3 = Product("Samsung TV", "55 inches, 4K", 50000.0, 7)
product_4 = Product("LG TV", "65 inches, OLED", 120000.0, 3)

category_1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
    [product_1, product_2],
)

category_2 = Category(
    "Телевизоры",
    "Современные телевизоры для дома",
    [product_3, product_4],
)

print(product_1.name)
print(category_1.name)
print(Category.category_count)
print(Category.product_count)
