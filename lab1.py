import doctest
from typing import Union


class Plant:
    condition = ("green", "gold", "gray")
    def __init__(self, name: str, color: str, seeds: float):
        """
        параментры - количество семян
                     название растения
                     цвет растения
        ошибки      - если название не str
                     если цвет не является str
        Примеры
        >>> a = Tree("oak", "green", 3.0000)
        >>> a.change_color("gold")
        >>> oak = Tree("oak", "green", 3.00)
        """
        self.seeds = 0
        self.generate_seeds(seeds)
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color
        if color not in self.condition:
            raise TypeError("Введите определенный цвет")

    def change_color(self, color: str) -> None:
        """
        функция меняет цвет дерева
        ошибки      - если название цвета не str
                     если цвет не входит в condition
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if color not in self.condition:
            raise TypeError("Введите определенный цвет")
        self.color = color


    def generate_seeds(self, seeds: float) -> None:
        """
        функция меняет количество семян
        ошибки      - если seeds не float
                      если seeds - отрицательное число
        """
        if not isinstance(seeds, float):
            raise TypeError("Семена должны быть float")
        if seeds < 0:
            raise ValueError("Семяна является отрицательным числом")

class Motorcycle:
    def __init__(self, price: float, max_speed: float):
        """
        объект "Мотоцикл"
        параметры - Цена мотоцикла
                    Маскимальная скорость мотоцикла
        """
        self.current_speed = 0
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price < 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость не может быть отрицательным числом или раняться нулю")
        self.max_speed = max_speed

    def init_speed(self, initial_speed: float) -> None:
        """
        функция задающая начальную скорость
        ошибка - если скорость не является int или float
                 если скорость является отрицательным числом
        """
        if not isinstance(initial_speed, (int, float)):
            raise TypeError("Начальную скорость должна быть типа int или float")
        if initial_speed < 0:
            raise ValueError("Начальную скорость не может быть отрицательным числом или раняться нулю")
        self.current_speed = initial_speed

    def to_current_speed(self, increase: int) -> None:
        """
        функция увелиивающая текущую скоость автомобиля
        ошибка - если доп. скорость не является int или float
                 если  доп. скорость является отрицательным числом
        """
        if not isinstance(increase, int):
            raise TypeError("Добавочая скорость должна быть типа int или float")
        if increase < 0 or self.current_speed + increase > self.max_speed:
            raise ValueError(
                "Добавочая скорость не может быть отрицательным числом или раняться нулю. Также, нельзя певышать максимальную скорость")
        self.current_speed += increase


    def cur_speed(self) -> float:
        """
        Функция, возвращающая текущую скорость
        >>> Yamaha = Motorcycle(5000000, 400)
        >>> Yamaha.init_speed(30)
        >>> Yamaha.to_current_speed(3)
        >>> Yamaha.cur_speed()
        """
        return self.current_speed


class Im_number:
    def __init__(self, real_part: Union[int, float], im_part: Union[int, float]):
        """
        Объект "Комплексное число"
        Парметры - real_part: реальная часть числа
                   im_part: мнимая часть числа
        Ошибки -  если реальная часть числа отлична от int или float.
                    если мнимая часть числа отлична от int или float.
        """
        if not isinstance(real_part, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        self.real = real_part
        if not isinstance(im_part, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        self.im = im_part

    def __add__(self, other: "Im_number") -> "Im_number" :
        """
        Функция сложения двух комплексных чисел
        """
        return Im_number(self.real+other.real, self.im+other.im)

    def show(self) -> None:
        """
        Функция вывода комплексного числа в консоль
        Примеры
        >>> first = Im_number(6, 50)
        >>> second = Im_number(6, 50)
        >>> third = first + second
        >>> third.show()
        """
        if self.im >= 0:
            print(f"{self.real} + i{self.im}")
        else:
            print(f"{self.real} - i{abs(self.im)}")



if __name__ == "__main__":
    doctest.testmod()