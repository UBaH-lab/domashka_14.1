from src.category import Category
from src.product import Product


product_1 = Product("iPhone 15", "256GB, Gray color", 210000.0, 8)
product_2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category_1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
    [product_1, product_2],
)

print(product_1.name)
print(category_1.name)
print(Category.category_count)
print(Category.product_count)