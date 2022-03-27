class Tomato:
    index: int
    ripeness: str
    states = {0: "Отсутствует", 1: "Цветение", 2: "Зеленый", 3: "Красный"}

    def __init__(self, index=0):
        self.index = index
        self.ripeness = self.states[index]

    def grow(self):
        if self.index < 3:
            self.index += 1
