class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        #поскольку имя автора и название книги по условию не изменяются, то проводим проверку в __init__
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self._name = name
        
        if not isinstance(author, str):
            raise TypeError("Имя автора книги должно быть типа str")
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        #число страниц может изменяться - делаем проверку в отдельной функции
        self.pages = pages
    
    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        #продолжительность может изменяться - делаем проверку в отдельной функции
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        if not isinstance(new_duration, (int, float)):
            raise TypeError("Продолжительность должна быть типа int или float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"