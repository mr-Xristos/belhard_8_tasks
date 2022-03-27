"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year):
        self.__author = author
        self.__title = title
        self.__year = year

    def __lt__(self, year):
        return self < year

    def __gt__(self, year):
        return self > year

    def __le__(self, year):
        return self <= year


    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, value: str):
        self.__author = value
        if not isinstance(value, str):
            raise ValueError


    @title.setter
    def title(self, value: str):
        self.__title = value
        if not isinstance(value, str):
            raise ValueError

    @year.setter
    def year(self, value: int):
        self.__year = value
        if not isinstance(value, int):
            raise ValueError

        elif CURRENT_YEAR < value:
            raise ValueError

        elif value <= 0:
            raise ValueError



