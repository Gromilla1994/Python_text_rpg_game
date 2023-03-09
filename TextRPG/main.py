from classes import *
from battle_system import *
import items
items.init()

hero = Hero("Zahar", 100, 10, "Warrior", [items.rusty_axe, items.barn_door])

dog = Enemy("Dog", 15, 3)

health_poison = Poison("Big health poison", "heal 50 hp", 50)

StartFigth(hero, dog)
