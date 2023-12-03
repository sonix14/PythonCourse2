# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Book:
    def __init__(self, name: str, count_of_pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param name: Имя книги
        :param count_of_pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Alphabet", 35)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип string")
        if name == "":
            raise ValueError("Имя не должно быть пустым")
        self.name = name

        if not isinstance(count_of_pages, int):
            raise TypeError("Количество страниц должно иметь тип int")
        if count_of_pages <= 0:
            raise ValueError("Количество страниц не должно быть меньше или равным 0")
        self.count_of_pages = count_of_pages

    def print_book(self) -> None:
        """
        Функция, которая выводит содержимое книги

        Примеры:
        >>> book = Book("Alphabet", 35)
        >>> book.print_book()
        """
        ...

    def rate_book(self, grade: int) -> None:
        """
        Функция, которая выставляет оценку книге

        :param grade: Оценка книги

        :raise ValueError: Если оценка выходит за параметры оценивания, то вызываем ошибку

        Примеры:
        >>> book = Book("Alphabet", 35)
        >>> book.rate_book(5)
        """
        if not isinstance(grade, int):
            raise TypeError("Выставляемая оценка должна быть типа int")
        if grade < 0 or grade > 5:
            raise ValueError("Выставляемая оценка должна находится в рамках оценивания - от 0 до 5")
        ...


class Shelf:
    def __init__(self, height: Union[int, float], width: Union[int, float], count_of_books: int):
        """
        Создание и подготовка к работе объекта "Полка"

        :param height: Высота, на которой расположена полка
        :param width: Ширина полки
        :param count_of_books: Количество книг на полке

        Примеры:
        >>> shelf = Shelf(100, 32, 5)  # инициализация экземпляра класса
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота расположения полки должна быть типа int или float")
        if height < 0:
            raise ValueError("Высота расположения полки должна быть положительным числом")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина полки должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина полки не должна быть меньше или равной 0")
        self.width = width

        if not isinstance(count_of_books, int):
            raise TypeError("Количество книг на полке должно иметь тип int")
        if count_of_books < 0:
            raise ValueError("Количество книг на полке должно быть положительным числом")
        self.count_of_books = count_of_books

    def move_shelf_horizontally(self, indent: Union[int, float]) -> bool:
        """
        Функция, которая перемещает полку по горизонтали

        :param indent: Число, на которое нужно отступить по горизонтали и переместить туда полку

        :return: Удалось ли переместить полку

        Примеры:
        >>> shelf = Shelf(100, 32, 5)
        >>> shelf.move_shelf_horizontally(4.5)
        """
        if not isinstance(indent, (int, float)):
            raise TypeError("Отсутуп должен быть типа int или float")
        ...

    def move_shelf_vertically(self, new_height: Union[int, float]) -> bool:
        """
        Функция, которая перемещает полку по вертикали

        :param new_height: Число, на которое нужно отступить по вертикали и переместить туда полку

        :return: Удалось ли переместить полку

        Примеры:
        >>> shelf = Shelf(100, 32, 5)
        >>> shelf.move_shelf_vertically(6)
        """
        if not isinstance(new_height, (int, float)):
            raise TypeError("Новая высота должна быть типа int или float")
        ...

    def take_book_from_shelf(self, book_name: str) -> Book:
        """
        Функция, которая достает с полки определенную книгу

        :param book_name: Имя книги, которую нужно взять с полки

        :raise ValueError: Если имя книги пустое, то вызываем ошибку

        :return: Книга, которую взяли с полки

        Примеры:
        >>> shelf = Shelf(100, 32, 5)
        >>> shelf.take_book_from_shelf("Alphabet")
        """
        if not isinstance(book_name, str):
            raise TypeError("Имя книги должно иметь тип string")
        if book_name == "":
            raise ValueError("Имя книги не должно быть пустым")
        ...

class Bookcase:
    def __init__(self, count_of_books: int, count_of_shelves: int):
        """
        Создание и подготовка к работе объекта "Книжный шкаф"

        :param count_of_books: Количество книг в шкафу
        :param count_of_shelves: Количество полок в шкафу

        Примеры:
        >>> bookcase = Bookcase(30, 3)  # инициализация экземпляра класса
        """
        if not isinstance(count_of_books, int):
            raise TypeError("Количество книг должно иметь тип int")
        if count_of_books < 0:
            raise ValueError("Количество книг должно быть положительным числом")
        self.count_of_books = count_of_books

        if not isinstance(count_of_shelves, int):
            raise TypeError("Количество полок должно иметь тип int")
        if count_of_shelves <= 0:
            raise ValueError("Количество полок не должно быть меньше или равным 0")
        self.count_of_shelves = count_of_shelves

    def put_book_in_bookcase(self, new_book_name: str, shelf_number: int) -> bool:
        """
        Функция, которая кладет новую кнингу в шкаф

        :param new_book_name: Имя книги, которую нужно положить в шкаф
        :param shelf_number: Номер полки, на котрую нужно положить книгу

        :raise ValueError: Если имя новой книги пустое, то вызываем ошибку
        :raise ValueError: Если номер полки меньше или равно 0, то вызываем ошибку

        :return: Удалось ли положить книгу в шкаф

        Примеры:
        >>> bookcase = Bookcase(30, 3)
        >>> bookcase.put_book_in_bookcase("Dictionary", 2)
        """
        if not isinstance(new_book_name, str):
            raise TypeError("Имя книги должно иметь тип string")
        if new_book_name == "":
            raise ValueError("Имя книги не должно быть пустым")

        if not isinstance(shelf_number, int):
            raise TypeError("Номер полки должен иметь тип int")
        if shelf_number <= 0:
            raise ValueError("Номер полки не должен быть меньше или равным 0")
        ...

    def take_book_from_bookcase(self, book_name: str) -> Book:
        """
        Функция, которая достает из шкафа определенную книгу

        :param book_name: Имя книги, которую нужно взять из шкаафа

        :raise ValueError: Если имя книги пустое, то вызываем ошибку

        :return: Книга, которую взяли из шкафа

        Примеры:
        >>> bookcase = Bookcase(30, 3)
        >>> bookcase.take_book_from_bookcase("Alphabet")
        """
        if not isinstance(book_name, str):
            raise TypeError("Имя книги должно иметь тип string")
        if book_name == "":
            raise ValueError("Имя книги не должно быть пустым")
        ...

    def clean_bookcase(self) -> None:
        """
        Функция, которая очищает шкаф от всех книг

        Примеры:
        >>> bookcase = Bookcase(30, 3)
        >>> bookcase.clean_bookcase()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
