BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("ID должно иметь тип int")
        if id_ < 0:
            raise ValueError("ID не должно быть меньше 0")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип string")
        if name == "":
            raise ValueError("Имя не должно быть пустым")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно иметь тип int")
        if pages <= 0:
            raise ValueError("Количество страниц не должно быть меньше или равным 0")
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            books = list()
        self.books = books

    def get_next_book_id(self):
        count = len(self.books)
        if count == 0:
            return 1
        else:
            return self.books[count-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        for i, val in enumerate(self.books, start=0):
            if val.id == book_id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
