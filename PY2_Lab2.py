class Book:
    def __init__(self, id_ : int, name : str, pages : int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: уникальный номер книги
        :param name: название книги
        :param pages: количество страниц
        
        Примеры:
        >>> oblomov = Book(123, 'Обломов', 842)  # инициализация экземпляра класса
        """
        if not isinstance(id_, int):
            raise TypeError("Уникальный номер (id) должен быть типа int")
        if id_ <= 0:
            raise ValueError("Уникальный номер (id) должен быть положительным числом")
        self.id = id_

        if not isinstance(name, str):
            raise TypeError("Наименование книги (name) должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц (pages) должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц (pages) должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


class Library:
    def __init__(self, books : list[Book] = None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: список книг, созданный из классов Book
        
        Примеры:
        >>> oblomov = Book(123, 'Обломов', 842)
        >>> list_of_books = [oblomov]
        >>> library_spb = Library(list_of_books)  # инициализация экземпляра класса
        """
        if books is None:
            books = []
        if not isinstance(books, list):
            raise TypeError("Список книг (books) должен быть типа list")
        for book_ in books:
            if not isinstance(book_, Book):
                raise TypeError("В списке книг (books) присутствуют элементы, отличные от класса Book")
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Функция позволяет получить уникальный порядковый id

        Пример:
        >>> library_spb = Library(list_of_books)
        >>> library_spb.get_next_book_id()      
        """
        if len(self.books) == 0:
            return 1
        
        #сортируем книги по их id
        self.books.sort(key=lambda x: x.id)
        
        return self.books[-1].id + 1
    
    def get_index_by_book_id(self, need_id : int) -> int:
        """
        Функция позволяет получить порядковый номер книги в списке, по его id.
        Сортировка в списке производится по возрастанию id.
        :param need_id: уникальный номер (id) для поиска

        Пример:
        >>> library_spb = Library(list_of_books)
        >>> library_spb.get_index_by_book_id(56)      
        """
        if not isinstance(need_id, int):
            raise TypeError("Уникальный номер (need_id) должен быть типа int")
        if need_id <= 0:
            raise ValueError("Уникальный номер (need_id) должен быть положительным числом")

        #сортируем книги по их id
        self.books.sort(key=lambda x: x.id)

        for index_, book_ in enumerate(self.books):
            if book_.id == need_id:
                return index_
        raise ValueError("Книги с запрашиваемым id не существует")