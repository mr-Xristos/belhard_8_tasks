from tomato import Tomato


class TomatoBush:

    tomato_list: list
    it_is_ripe = False

    def __init__(self, *args):
        self.tomato_list = list(a for a in args)

    def grow_all(self):
        for x in self.tomato_list:
            x.grow()

    def all_are_ripe(self):
        self.it_is_ripe = True
        for x in self.tomato_list:
            if x.is_ripe() is not True:
                self.it_is_ripe = False
                return False
        return True

    def give_away_all(self):
        ripe_tomato = self.tomato_list
        if self.it_is_ripe:
            self.tomato_list = []
        return ripe_tomato
