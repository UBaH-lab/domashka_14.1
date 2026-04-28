from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.category import Category
    from src.product import Product


class CategoryIterator:
    """Итератор для перебора товаров категории."""

    def __init__(self, category: "Category") -> None:
        """Инициализирует итератор."""
        self._products = category._get_products()
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        """Возвращает итератор."""
        return self

    def __next__(self) -> "Product":
        """Возвращает следующий продукт."""
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product
