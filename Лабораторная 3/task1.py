from typing import Final


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name: Final = name
        self._author: Final = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно иметь тип int")
        if pages <= 0:
            raise ValueError("Количество страниц не должно быть меньше или равным 0")
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    @property
    def duration(self) -> int:
        return self.duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна иметь тип float")
        if duration <= 0.0:
            raise ValueError("Продолжительность аудиокниги не должна быть меньше или равной 0")
        self.duration = duration
