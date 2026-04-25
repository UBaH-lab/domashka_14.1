from src.product import Product
from src.category_iterator import CategoryIterator


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализирует объект категории."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута products. Возвращает строку."""
        result = ""
        for product in self.__products:
            result += f"{product}\n"
        return result

    def _get_products(self) -> list[Product]:
        """Возвращает список продуктов (для итератора)."""
        return self.__products

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> CategoryIterator:
        """Возвращает итератор по продуктам категории."""
        return CategoryIterator(self)
