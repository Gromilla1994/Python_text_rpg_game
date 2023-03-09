from classes import *
import hepl_functions

action_variants = {
    "ударить": bcolors.FAIL,
    "открыть инвентарь": bcolors.WARNING,
    "попытаться убежать": bcolors.OKGREEN
}

formating_action_variants = []  

for key in action_variants:
    formating_action_variants.append(action_variants[key] + key)

def StartFigth(hero: Hero, enemy: Enemy):
    print(f"{hero.name}, на тебя напал {enemy.name}")
    print("Ты можешь: \n{0}".format(" : ".join(formating_action_variants)) + bcolors.ENDC)
    answer = hepl_functions.validateAnswer(action_variants, True)

    if answer == "ударить":
        enemy.health_points -= hero.attack_power
        print(f"\nТы нанёс врагу {enemy.name} {hero.attack_power} урона!\nЗдоровье врага {enemy.name} = {enemy.health_points if enemy.health_points >= 0 else '0'}!")
    
    elif answer == "открыть инвентарь":
        hero.PrintInfo()

    elif answer == "попытаться убежать":
        print(f"Ты убежал от {enemy.name}")
        return  