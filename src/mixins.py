class LogMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Инициализирует объект и печатает информацию о создании."""
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект класса {self.__class__.__name__} "
            f"с параметрами: args={args}, kwargs={kwargs}"
        )

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.__class__.__name__}({self.__dict__})"
