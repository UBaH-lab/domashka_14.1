from src.base_unit import BaseUnit
from src.product import Product


class Order(BaseUnit):
    """Класс для представления заказа."""

    def __init__(
        self,
        name: str,
        description: str,
        product: Product,
        quantity: int,
    ) -> None:
        """Инициализирует объект заказа."""
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        """Вычисляет итоговую стоимость заказа."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return (
            f"Заказ: {self.name}\n"
            f"Товар: {self.product.name}\n"
            f"Количество: {self.quantity} шт.\n"
            f"Итого: {self.total_price} руб."
        )
