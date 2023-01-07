import doctest

class MusicColumn:
    def __init__(self, max_volume : int, brand : str):
        """
        Создание и подготовка к работе объекта "Музыкальная колонка"
        :param max_volume: максимальная громкость колонки
        :param brand: название производителя
        
        Примеры:
        >>> MusicColumn = MusicColumn(100, 'Алиса')  # инициализация экземпляра класса
        """
        if not isinstance(max_volume, int):
            raise TypeError("Максимальная громкость должна быть типа int")
        if max_volume <= 0:
            raise ValueError("Максимальная громкость должна быть положительным числом")
        self.max_volume = max_volume

        if not isinstance(brand, str):
            raise TypeError("Название бренда должно быть типа str")
        self.brand = brand
               
        self.max_battery = 100
        self.current_volume = 0

    def increase_the_volume(self) -> None:
        """
        Увеличить громкость на одно деление. 
        Одно деление равняется 10% от максимальной громкости.
        Громкость не может быть больше максимальной.

        Пример:
        >>> alisa = MusicColumn(100, 'Алиса')
        >>> alisa.increase_the_volume()
        """
        ...

    def reduce_the_volume(self) -> None:
        """
        Уменьшить громкость на одно деление. 
        Одно деление равняется 10% от максимальной громкости.
        Громкость не может быть меньше 0.

        Пример:
        >>> alisa = MusicColumn(100, 'Алиса')
        >>> alisa.reduce_the_volume()
        """
        ...

    def check_battery(self) -> int:
        """
        Проверка уровня зарядки колонки в целочисленных процентах.

        Пример:
        >>> alisa = MusicColumn(100, 'Алиса')
        >>> alisa.check_battery()
        """
        ...


class Discussion:
    def __init__(self, topic : str, participants : list) -> None:
        """
        Создание и подготовка к работе объекта "Чат"
        :param topic: название чата
        :param participants: участники (больше одного)
        
        Примеры:
        >>> Discussion = Discussion("Группа 462", ['Смирнов Олег Юрьевич', 'Любимова Татьяна Юрьевна'])  # инициализация экземпляра класса
        """
        if not isinstance(topic, str):
            raise TypeError("Название чата должно быть типа str")
        self.topic = topic

        if not isinstance(participants, list):
            raise TypeError("Состав участников чата должен быть представлен в виде list")
        if len(participants) <= 1:
            raise ValueError("Участников чата должно быть больше одного")
        self.participants = participants

    def add_participant(self, new_participants : list) -> None:
        """
        Добавление участника(-ов) в чат
        
        :param new_participants: Список участников к добавлению
        :raise TypeError: Если участники записаны не в виде списка, то вызываем ошибку
        :raise ValueError: Если количество участников равно 0, то вызываем ошибку

        Пример:
        >>> chat_462 = Discussion("Группа 462", ['Смирнов Олег Юрьевич', 'Любимова Татьяна Юрьевна'])
        >>> chat_462.add_participant(['Злой Змей Горыныч'])
        """
        ...

    def delete_participant(self, participants_to_delete : list) -> None:
        """
        Удаление участника(-ов) из чата

        :param participants_to_delete: Список участников к удалению
        :raise TypeError: Если участники записаны не в виде списка, то вызываем ошибку
        :raise ValueError: Если список будет включать всех текущих участников, то вызываем ошибку

        Пример:
        >>> chat_462 = Discussion("Группа 462", ['Смирнов Олег Юрьевич', 'Любимова Татьяна Юрьевна', 'Злой Змей Горыныч'])
        >>> chat_462.delete_participant(['Злой Змей Горыныч'])
        """
        ...

    def change_topic(self, new_topic : str) -> None:
        """
        Смена назавания чата

        :param new_topic: Новое название чата
        :raise TypeError: Если новое название не имеет тип str, то вызываем ошибку

        Пример:
        >>> chat_462 = Discussion("Группа 462", ['Смирнов Олег Юрьевич', 'Любимова Татьяна Юрьевна'])
        >>> chat_462.change_topic('Группа 462 (2022)')
        """
        ...


class Weapon:
    def __init__(self, damage : int, weight : float, level : int) -> None:
        """
        Создание и подготовка к работе объекта "Оружие"
        :param damage: урон, наносимый оружием
        :param weight: вес оружия
        :param level: уровень оружия
        
        Примеры:
        >>> sword = Weapon(10, 5.4, 3)  # инициализация экземпляра класса
        """
        if not isinstance(damage, int):
            raise TypeError("Урон оружия должен быть типа int")
        if damage <= 0:
            raise ValueError("Урон оружия должен быть положительным числом")
        self.damage = damage

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес оружия должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес оружия должен быть положительным числом")
        self.weight = weight

        if not isinstance(level, int):
            raise TypeError("Уровень оружия должен быть типа int")
        if level <= 0:
            raise ValueError("Уровень оружия должен быть положительным числом")
        self.level = level

    def up_damage(self, upgrade : int) -> None:
        """
        Увеличивает урон оружия.

        :param upgrade: На сколько единиц повышается урон оружия
        :raise TypeError: Если добавленный урон не является int, то вызываем ошибку

        Пример:
        >>> sword = Weapon(10, 5.4, 3)
        >>> sword.up_damage(2)
        """
        ...
    
    def up_weight(self, upgrade : float) -> None:
        """
        Увеличивает вес оружия.

        :param upgrade: На сколько единиц увеличивается вес оружия
        :raise TypeError: Если вес для добавления не является int или float, то вызываем ошибку

        Пример:
        >>> sword = Weapon(10, 5.4, 3)
        >>> sword.up_weight(0.2)
        """
        ...

    def down_weight(self, upgrade : float) -> None:
        """
        Уменьшает вес оружия.
        
        :param upgrade: На сколько единиц уменьшается вес оружия
        :raise TypeError: Если вес для убавления не является int или float, то вызываем ошибку
        :raise ValueError: Если убавляемый вес больше или равен текущему весу, то вызываем ошибку

        Пример:
        >>> sword = Weapon(10, 5.4, 3)
        >>> sword.down_weight(0.4)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()