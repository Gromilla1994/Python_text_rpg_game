from classes import *
import hepl_functions
import random

action_variants = {
    "ударить": bcolors.FAIL,
    "открыть инвентарь": bcolors.WARNING,
    "попытаться убежать": bcolors.OKGREEN
}

formating_action_variants = hepl_functions.addColorToStrings(action_variants) 

def StartFigth(hero: Hero, enemy: Enemy):
    print(f"{hero.name}, на тебя напал {enemy.name}")
    while hero.health_points > 0 and enemy.health_points > 0:
        hero.PrintInfo()
        answer = hepl_functions.validateAnswer(action_variants, True)

        if answer == "ударить":
            hero_weapon = hero.equiped_weapon 
            # если на персонаже эквипированно оружие, то атака перса складывается с ней, иначе в счет идёт просто атака персонажа
            attack_power = (hero.attack_power + hero_weapon.attack_power) if hero_weapon != "" else hero.attack_power  
            enemy.health_points -= attack_power
            
            print(f"\nТы нанёс врагу {enemy.name} {attack_power} урона!\nЗдоровье врага {enemy.name} = {enemy.health_points if enemy.health_points >= 0 else '0'}!")
        
        elif answer == "открыть инвентарь":
            hero.OpenInventory()

        elif answer == "попытаться убежать":
            if runFromEnemy(50):
                print(f"Ты убежал от {enemy.name}")
                return
            print("Убежать не удалось!")
                  
        
        hero.health_points -= enemy.attack_power
        print(f"{enemy.name} нанёс тебе {enemy.attack_power} ед. урона!\n")

def runFromEnemy(success_chance):
    if success_chance >= random.randint(1, 100):
        return True
    
    return False 
    