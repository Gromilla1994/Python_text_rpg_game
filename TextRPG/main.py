from classes import *
from battle_system import *
import items
items.init()

inventory = [
    items.weapons_list["rusty_axe"],
    items.weapons_list["barn_door"],
]

hero = Hero("Zahar", 100, 10, "Warrior", inventory)
dog = Enemy("Dog", 15, 3)
health_poison = Poison("Big health poison", "heal 50 hp", 50)

hero.OpenInventory()
