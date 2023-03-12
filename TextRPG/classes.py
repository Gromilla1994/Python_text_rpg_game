import hepl_functions

# colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Item classes
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @hepl_functions.pretify_separation
    def PrintInfo(self):
        name = bcolors.OKCYAN + f"{self.name}"
        description = bcolors.ENDC + f"{self.description}"

        print(name + "\n" + description)


class MeleeWeapon(Item):
    def __init__(self, name: str, description: str, attack_power):
        super().__init__(name, description)
        self.attack_power = attack_power 


class Shield(Item):
    def __init__(self, name: str, description: str, protection_power):
        super().__init__(name, description)
        self.protection_power = protection_power

class Poison(Item):
    def __init__(self, name, description, health_regeneration_points: int):
        Item.__init__(self, name, description)
        self.health_regeneration_points = health_regeneration_points
    
    def Activate(self, entity):
        super().Activate()
        entity.health_points += self.health_regeneration_points


# Entity classes
class Entity:
    def __init__(self, name: str, health_points: int, attack_power: int):
        self.name = name
        self.health_points = health_points
        self.attack_power = attack_power

    def PrintInfo(self):
        name = bcolors.HEADER + f"name - {self.name}"
        health_points = bcolors.OKGREEN + f"health points - {self.health_points}"
        attack_power = bcolors.FAIL + f"attack power - {self.attack_power}"
        
        info_array = [name, health_points, attack_power]
        print(" : ".join(info_array))

    def Attack(self, target):
        target.health_points -= self.attack_power 

    def ActivateItem(self, item: Item):
        item.Activate(self)


class Hero(Entity):
    def __init__(self, name: str, heath_points: int, attack_power: int, class_name: str, inventory=[]):
        Entity.__init__(self, name, heath_points, attack_power)
        self.class_name = class_name
        self.inventory = inventory

    def UseItem(self):
        item_name = input("Какой предмет хочешь использовать?:")
        
    def AppendItemInInventory(self, item: Item):
        self.inventory.append(item)

    @hepl_functions.pretify_separation
    def PrintInfo(self):
        super().PrintInfo()

        names_of_item_in_inventory = ""
        for item in self.inventory:
            names_of_item_in_inventory += "\n" + item.name

        print(bcolors.ENDC + "inventory:{0}".format(names_of_item_in_inventory))

    def OpenInventory(self):
        action = ""

        while action != "выйти":
            self.PrintInfo()
            action = hepl_functions.validateAnswer(["экипировать предмет", "использовать предмет", "выйти"], False)


class Enemy(Entity):
    def __init__(self, name: str, heath_points: int, attack_power: int):
        Entity.__init__(self, name, heath_points, attack_power)