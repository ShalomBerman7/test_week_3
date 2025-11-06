from random import randint
from core.orc import Orc


class Goblin(Orc):
    def __init__(self, name, hp, type, speed, power, armor_rating, weapon):
        super().__init__(name, hp, type, speed, power, armor_rating, weapon)

    def speak(self):
        return f'I Mr {self.name} {self.type}, I will break your bones.'

    def attack(self):
        n = randint(1, 20)
        n += self.speed

    def run_away(self):
        pass


def rand_speed():
    n = randint(5,10)
    return n

def rand_power():
    n = randint(5,10)
    return n

def rand_weapon():
    w = ['knife', 'sword', 'axe']
    n = randint(0,2)
    return w[n]

gob = Goblin('Kanius', 20, 'goblin', rand_speed(), rand_power(), 1, rand_weapon())
