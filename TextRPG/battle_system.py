from classes import *
import hepl_functions

action_variants = {
    "ударить": bcolors.FAIL,
    "открыть инвентарь": bcolors.WARNING,
    "попытаться убежать": bcolors.OKGREEN
}

formating_action_variants = hepl_functions.addColorToStrings(action_variants) 

def StartFigth(hero: Hero, enemy: Enemy):
    print(f"{hero.name}, на тебя напал {enemy.name}")
    answer = hepl_functions.validateAnswer(action_variants, True)

    if answer == "ударить":
        enemy.health_points -= hero.attack_power
        print(f"\nТы нанёс врагу {enemy.name} {hero.attack_power} урона!\nЗдоровье врага {enemy.name} = {enemy.health_points if enemy.health_points >= 0 else '0'}!")
    
    elif answer == "открыть инвентарь":
        hero.DisplayInventory()

    elif answer == "попытаться убежать":
        print(f"Ты убежал от {enemy.name}")
        return  