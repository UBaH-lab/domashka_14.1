class Product:
    """Класс для представления продукта."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализирует объект продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
