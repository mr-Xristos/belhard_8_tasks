from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener
import gardener
import tomato
import tomato_bush

if __name__ == '__main__':
    tomat1 = tomato.Tomato(1)
    tomat2 = tomato.Tomato(2)
    tomat3 = tomato.Tomato(3)
    tomat4 = tomato.Tomato(4)
    tomat5 = tomato.Tomato(5)

    bush1 = tomato_bush.TomatoBush(tomat2, tomat3, tomat5)
    bush2 = tomato_bush.TomatoBush(tomat1, tomat4)

    gardener123 = gardener.Gardener('egor', bush2, bush1)

    gardener123.work()
    print(gardener123.harvest())
