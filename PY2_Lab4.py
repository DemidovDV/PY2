import doctest

class Tank:
    def __init__(self, name : str, max_speed : float) -> None: 
        """
        Создание и подготовка к работе объекта "Танк"
        :param name: название танка
        :param max_speed: максимальная скорость танка, км/ч

        Примеры:
        >>> IS_6 = Tank('ИС-6', 42.5)  # инициализация экземпляра класса
        """
        
        if not isinstance(name, str):
            raise TypeError("Название танка должно быть типа str")
        self._name = name
        
        self.max_speed = max_speed
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def max_speed(self) -> float:
        return self._max_speed
    
    @max_speed.setter
    def max_speed(self, new_max_speed) -> None:
        if not isinstance(new_max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if new_max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self._max_speed = new_max_speed
    
    def contusion_of_a_mechanic(self, degree_of_contusion=0.5) -> None:
        """
        Снижение максимальной скорости на n% в связи с контузией механика-водителя.

        :param degree_of_contusion: отрицательный эффект контузии на максимальную скорость в процентах.
        Значение процентов описывается десятичной дробью (50% указывается как 0.5).
        Значение должно быть в пределах от 0 до 50%. По умолчанию - 50%.

        Пример:
        >>> IS_6 = Tank('ИС-6', 42.0)
        >>> IS_6.contusion_of_a_mechanic(0.3) #максимальная скорость снизится на 30%
        """
        if not isinstance(degree_of_contusion, (int, float)):
            raise TypeError("Отрицательный эффект контузии может быть типа int или float")
        if not 0 <= degree_of_contusion <= 0.5:
            raise ValueError("Отрицательный эффект контузии должен находится в пределах от 0 до 50%")

        self.max_speed = round(self.max_speed * (1 - degree_of_contusion), 2)

    def fuel_effect(self) -> None:
        """
        Увеличение базовой максимальной скорости за счет качественного топлива.
        Эффект - рост максимальной скорости +10%

        Пример:
        >>> IS_6 = Tank('ИС-6', 42.0)
        >>> IS_6.fuel_effect() #максимальная скорость увеличится на 10%
        """
        self.max_speed = self.max_speed * 1.1

    def __str__(self) -> str:
        return f'Танк {self._name}'
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, max_speed={self.max_speed!r})"



class SiegeModeTank(Tank):
    def __init__(self, name: str, max_speed: float, max_speed_in_siege_mode : float):
        """
        Создание и подготовка к работе объекта "Танк c осадным механизмом"
        :param name: название танка
        :param max_speed: максимальная скорость танка, км/ч
        :param max_speed_in_siege_mode: максимальная скорость танка в осадном режиме, км/ч

        Примеры:
        >>> Strv_103B = SiegeModeTank('Strv 103B', 60, 20)  # инициализация экземпляра класса
        """
        super().__init__(name, max_speed)
        
        if not isinstance(max_speed_in_siege_mode, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed_in_siege_mode <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self._max_speed_in_siege_mode = max_speed_in_siege_mode
    
    @property
    def max_speed_in_siege_mode(self) -> int:
        return self._max_speed_in_siege_mode

    def transition_to_siege_mode(self) -> None:
        """
        Изменение максимальной скорости танка при переходе в осадный режим

        Примеры:
        >>> Strv_103B = SiegeModeTank('Strv 103B', 60, 20)  # инициализация экземпляра класса
        >>> Strv_103B.transition_to_siege_mode()
        """
        self.max_speed = self._max_speed_in_siege_mode
    
    #перегруженный метод
    def fuel_effect(self) -> None:
        """
        Увеличение базовой максимальной скорости за счет качественного топлива.
        Эффект - рост максимальной скорости +10%. Эффект не увеличивает максимальную скорость в осадном режиме.

        Пример:
        >>> Strv_103B = SiegeModeTank('Strv 103B', 60, 20)  # инициализация экземпляра класса
        >>> Strv_103B.fuel_effect()                         # максимальная скорость составит 66 км/ч

        >>> Strv_103B.transition_to_siege_mode()
        >>> Strv_103B.fuel_effect()                         # максимальная скорость составит 20 км/ч
        """
        if self.max_speed != self._max_speed_in_siege_mode:
            self.max_speed = self.max_speed * 1.1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, max_speed={self.max_speed!r}, max_speed_in_siege_mode={self._max_speed_in_siege_mode!r})"

    #метод __str__ наследуется от родительского класса



""" Тестирование """
#проверка базовых сценариев
if __name__ == "__main__":
    doctest.testmod()


#Создание проверок (для проверки сделаем максимальную скорость танков одинаковой)
#1. функция класса Tank contusion_of_a_mechanic корректно работает
def check_contusion_of_a_mechanic():
    IS_6 = Tank('ИС-6', 60)
    Strv_103B = SiegeModeTank('Strv 103B', 60, 20)

    IS_6.contusion_of_a_mechanic()
    Strv_103B.contusion_of_a_mechanic()
    
    if IS_6.max_speed != Strv_103B.max_speed:
        print("ОШИБКА: функция класса Tank contusion_of_a_mechanic()")
        return False
    return True

#2. функция класса Tank contusion_of_a_mechanic корректно работает в осадном режиме
def check_contusion_of_a_mechanic_in_siege_mode():
    Strv_103B = SiegeModeTank('Strv 103B', 60, 20)

    Strv_103B.transition_to_siege_mode()
    Strv_103B.contusion_of_a_mechanic()
    
    if Strv_103B.max_speed != 10:
        print("ОШИБКА: функция класса Tank contusion_of_a_mechanic() в осадном режиме")
        return False
    return True
    
#3. функция класса Tank fuel_effect корректно работает 
def check_fuel_effect():
    IS_6 = Tank('ИС-6', 60)
    Strv_103B = SiegeModeTank('Strv 103B', 60, 20)

    IS_6.fuel_effect()
    Strv_103B.fuel_effect()
    
    if IS_6.max_speed != Strv_103B.max_speed:
        print("ОШИБКА: функция класса Tank fuel_effect")
        return False
    return True
    
#4. функция класса SiegeModeTank fuel_effect корректно работает в осадном режиме
def check_fuel_effect_in_siege_mode():
    Strv_103B = SiegeModeTank('Strv 103B', 60, 20)

    Strv_103B.fuel_effect()
    Strv_103B.transition_to_siege_mode()
    if Strv_103B.max_speed != 20:
        print("ОШИБКА: функция класса Tank fuel_effect в осадном режиме")
        return False
    
    Strv_103B = SiegeModeTank('Strv 103B', 60, 20)

    Strv_103B.transition_to_siege_mode()
    Strv_103B.fuel_effect()
    if Strv_103B.max_speed != 20:
        print("ОШИБКА: функция класса Tank fuel_effect в осадном режиме")
        return False
    return True
    
def check_all():
    final = []
    final.append(check_contusion_of_a_mechanic())
    final.append(check_contusion_of_a_mechanic_in_siege_mode())
    final.append(check_fuel_effect())
    final.append(check_fuel_effect_in_siege_mode())
    if all(final):
        print('Ошибки не найдены')

#запуск проверок
check_all()