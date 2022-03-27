import house
import person
import townhouse

if __name__ == '__main__':
    House1 = house.House('пр-т Партизанский 18', 50, 55000)
    House2 = house.House('пр-т люцинская 40', 29, 49000)

    Townhouse1 = townhouse.Townhouse('Грушевкая 44', 26000)
    Townhouse2 = townhouse.Townhouse('Казинца 38', 19800)

    Egor = person.Person('Egor', 25)
    Egor.make_deal(House2)
    Egor.info()
    Egor.earn_money(100000)
    Egor.info()
    Egor.make_deal(House2)
    Egor.info()

