# TODO:

# - систему убегания от врага, завязанную на рандоме - \[* *]/
# - пофиксить отображение надетого предмета - \[* *]/
# - сделать так, чтобы атака героя суммировалась с атакой оружия
# - создать бд вместо items.py 
# - систему награды за победу над мобом
# - систему торговли с вендором

# TODO:

from classes import *
from battle_system import *
import items
items.init()

inventory = [
    items.weapons_list["ржавый топор"],
    items.weapons_list["сломанный меч"],
    items.poison_list["зелье здоровья"]
]

hero = Hero("Zahar", 100, 10, "Warrior", inventory)
dog = Enemy("Dog", 15, 3)
Poison("Big health poison", "heal 50 hp", 50)

StartFigth(hero, dog)