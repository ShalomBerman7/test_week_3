from random import randint


class Orc:
    def __init__(self, name, hp, type, speed, power, armor_rating, weapon):
        self.name = name
        self.hp = hp
        self.type = type
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.weapon = weapon

    def speak(self):
        return f'Im {self.name} {self.type}, nervous, want to fight?'

    def attack(self):
        n = randint(1, 20)
        n += self.speed


def rand_speed():
    n = randint(0,5)
    return n

def rand_power():
    n = randint(10,15)
    return n

def rand_armor():
    n = randint(2,8)
    return n

def rand_weapon():
    w = ['knife', 'sword', 'axe']
    n = randint(0,2)
    return w[n]

orc = Orc('Miniscus', 50, 'orc', rand_speed(), rand_power(), rand_armor(), rand_weapon())
