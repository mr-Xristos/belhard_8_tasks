class House:

    address: str
    area: float
    cost: float

    def __init__(self, address, area, coast):
        self.address = address
        self.area = area
        self.cost = coast

    def increase_cost(self, money):
        self.cost += money

    def decrease_cost(self, money):
        self.cost -= money

