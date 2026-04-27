from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    name: str
    description: str
    __price: float
    quantity: int

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Абстрактный метод инициализации продукта."""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный сеттер для цены."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Абстрактный метод сложения продуктов."""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict[str, Any]) -> "BaseProduct":
        """Абстрактный метод создания продукта из словаря."""
        pass
