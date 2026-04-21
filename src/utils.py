import json

from src.category import Category
from src.product import Product


def load_data_from_json(filename: str) -> list[Category]:
    """Загружает категории и продукты из JSON-файла."""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        products = [
            Product.new_product(product)
            for product in category_data["products"]
        ]

        category = Category(
            category_data["name"],
            category_data["description"],
            products,
        )
        categories.append(category)

    return categories
