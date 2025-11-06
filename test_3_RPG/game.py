from random import randint
from core.player import p
from core.orc import orc
from core.goblin import gob


class Game:

    def start(self):
        choice = input(Game.show_menu(self))
        if choice == '1':
            return 'Lets go.'
        else:
            return 'bay'

    def show_menu(self):
        return f'Do you want to fight? \n 1. Yes \n 2. No'

    def create_player(self):
        return p

    def choose_random_monster(self):
        list_monster = [orc, gob]
        rand = randint(0,1)
        return list_monster[rand]


    def battle(player, monster):
        while p.hp >= 0 and monster.hp >= 0:


    def roll_dice(sides):
        dice = randint(1,sides)
        return dice

print(Game.roll_dice(6))

Game.battle(p,Game.choose_random_monster())
