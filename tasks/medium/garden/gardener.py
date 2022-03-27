class Gardener:

    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(plant for plant in args)

    def work(self):
        for plant in self.plants:
            plant.grow_all()

    def harvest(self):
        ripe_list = []
        for plant in self.plants:
            if plant.all_are_ripe():
                ripe_list.append(plant.give_away_all())
            else:
                print('Das tomaten nicht sozretten!')
                return None
        return ripe_list