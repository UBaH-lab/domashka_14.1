from abc import ABC, abstractmethod


class BaseUnit(ABC):
    """Абстрактный базовый класс для Category и Order."""

    name: str
    description: str

    @abstractmethod
    def __init__(self, name: str, description: str) -> None:
        """Абстрактный метод инициализации."""
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass
