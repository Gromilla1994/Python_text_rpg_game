# TODO:
# - систему убегания от врага, завязанную на рандоме
# 
#

from classes import *
from battle_system import *
import items
items.init()

inventory = [
    items.weapons_list["rusty_axe"],
    items.weapons_list["barn_door"],
    items.poison_list["health_poison"]
]

hero = Hero("Zahar", 100, 10, "Warrior", inventory)
dog = Enemy("Dog", 15, 3)
Poison("Big health poison", "heal 50 hp", 50)

StartFigth(hero, dog)