from random import randint


class Player:
    def __init__(self, name, hp, speed, power, armor_rating, profession):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.profession = profession

        if self.profession == 'Doctor':
            self.hp += 10
        else:
            self.power += 2

    def speak(self):
        return f'Hi, I {self.name}. I am very angry.'

    def attack(self):
        n = randint(1,20)
        n += self.speed


def rand_sp_po():
    n = randint(5,10)
    return n

def rand_armor():
    n = randint(5,15)
    return n

def rand_profession():
    l = ['Doctor', 'Warrior']
    n = randint(0,1)
    return l[n]

p = Player('mustang', 50, rand_sp_po(), rand_sp_po(), rand_armor(),rand_profession())
