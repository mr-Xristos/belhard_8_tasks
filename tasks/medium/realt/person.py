from house import House
from townhouse import Townhouse


class Person:
    name:str
    age: int
    money: int
    realty: list

# Методы:
#
# инициализатор __init__, который принимает name и age, присваивает их self.name и self.age
    # соответственно. self.cash присваивает 0, а self.realty присваивает пустой список
# метод info(), который будет выводить поля name, age, realty и money.
# метод earn_money(), который принимает значение, на которое нужно увеличить money
# метод make_deal(), который принимает объект класса House или Townhouse, и если у человека достаточно денег,
    # то списывает их с money и добавляет объект дома к self.realty

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(self.name, self.age, self.realty, self.money)

    def earn_money(self, plus_dengi):
        self.money += plus_dengi

    def make_deal(self, babki):
        if self.money >= babki.cost:
            self.money -= babki.cost
            self.realty.append(babki)
        else:
            print('нужно больше золота')




