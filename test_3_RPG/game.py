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


    def battle(player, monster):  #זה יותר פסאודו קוד מאשר קוד וגם הוא לא שלם אבל איבדתי את הראש אז ניסיתי לעשות מינימום
        mon = Game.roll_dice(20)
        mon += monster.speed
        ply = Game.roll_dice(20)
        ply += player.speed
        if ply >= mon:
            start = ply
        else:
            start = mon
        while p.hp >= 0 and monster.hp >= 0:
            boom = Game.roll_dice(20)
            boom += player.speed
            if boom > mon.armor_rating:
                faild = Game.roll_dice(6)
                faild += player.power
                mon.hp -= faild
                if mon.hp <= 0:
                    print(f'{player} Winner')
                    break
                else:
                    'מחליפים'
            else:
                'מחליפים'



    def roll_dice(sides):
        dice = randint(1,sides)
        return dice

print(Game.roll_dice(6))

Game.battle(p,Game.choose_random_monster(self=None))
