class Feline:
    def __init__(self, age: int, name: str):
        """
        Создание и подготовка к работе объекта "Царство кошачьих"

        :param age: Возраст представителя царства кошачьих
        :param name: Имя представителя царства кошачьих

        Примеры:
        >>> cat = Feline(2, "Barsic")  # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен иметь тип int")
        if age <= 0:
            raise ValueError("Возраст не должен быть меньше или равным 0")
        self._age = age

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип string")
        if name == "":
            raise ValueError("Имя не должно быть пустым")
        self._name = name

    def __str__(self):
        return f"Представитель кошачьих {self.name}. Возраст: {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__}(age={self.age!r}, name={self.name!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    def roar(self) -> None:
        """
        Функция, которая имитирует рык представителя кошачьего царства
        Установоена средняя громкость рыка

        Примеры:
        >>> cat = Feline(2, "Barsic")
        >>> cat.roar()
        """
        ...

    def play(self) -> None:
        """
        Функция, которая имитирует игру с представителем кошачьего царства

        Примеры:
        >>> cat = Feline(2, "Barsic")
        >>> cat.play()
        """
        ...


class Manul(Feline):
    def __init__(self, age: int, name: str, fluffiness_level: int):
        """
        Создание и подготовка к работе объекта "Манул"

        :param age: Возраст манула
        :param name: Имя манула
        :param fluffiness_level: Уровень пушистости

        Примеры:
        >>> manul = Manul(3, "Barsic", 4)  # инициализация экземпляра класса
        """
        super().__init__(age, name)

        if not isinstance(fluffiness_level, int):
            raise TypeError("Уровень пушистости должен иметь тип int")
        if fluffiness_level < 0 or fluffiness_level > 5:
            raise ValueError("Уровень пушистости должен находиться в рамках оценивания - от 0 до 5")
        self._fluffiness_level = fluffiness_level

    def __str__(self):
        return f"Манул {self.name}. Возраст: {self.age}. Уровень пушистости: {self.fluffiness_level}"

    def __repr__(self):
        return f"{self.__class__.__name__}(age={self.age!r}, name={self.name!r}, " \
               f"fluffiness_level={self.fluffiness_level!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def fluffiness_level(self) -> int:
        return self._fluffiness_level

    def roar(self) -> None:
        super().roar()

    def play(self) -> None:
        super().play()


class Lynx(Feline):
    def __init__(self, age: int, name: str):
        """
        Создание и подготовка к работе объекта "Рысь"

        :param age: Возраст рыси
        :param name: Имя рыси

        Примеры:
        >>> lynx = Lynx(3, "Barsic")  # инициализация экземпляра класса
        """
        super().__init__(age, name)

    def __str__(self):
        super().__str__()

    def __repr__(self):
        super().__repr__()

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    def roar(self) -> None:
        """
        Функция, которая имитирует рык рыси
        Метод перегружен с целью повышения уровня громкости рыка

        Примеры:
        >>> cat = Feline(2, "Barsic")
        >>> cat.roar()
        """
        ...

    def play(self) -> None:
        super().play()


if __name__ == "__main__":
    # Write your solution here
    pass
