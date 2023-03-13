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

    def Equip(self, hero):
        hero.equiped_weapon = self


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
        print(" : ".join(info_array) + bcolors.ENDC)

    def Attack(self, target):
        target.health_points -= self.attack_power 

    def ActivateItem(self, item: Item):
        item.Activate(self)


class Hero(Entity):
    def __init__(self, name: str, heath_points: int, attack_power: int, class_name: str, inventory=[], equiped_weapon=""):
        Entity.__init__(self, name, heath_points, attack_power)
        self.class_name = class_name
        self.inventory = inventory
        self.equiped_weapon = equiped_weapon

    def UseItem(self):
        item_name = input("Какой предмет хочешь использовать?:")
        
    def AppendItemInInventory(self, item: Item):
        self.inventory.append(item)

    @hepl_functions.pretify_separation
    def PrintInfo(self):
        super().PrintInfo()

    @hepl_functions.pretify_separation
    def DisplayInventory(self, classes_of_items=[]):
        names_of_item_in_inventory = []

        if classes_of_items != []:
            for item in self.inventory:
                if item.__class__.__name__ in classes_of_items:
                    names_of_item_in_inventory.append(item.name)
        else:
            for item in self.inventory:
                names_of_item_in_inventory.append(item.name)

        print(bcolors.ENDC + ("\n".join(names_of_item_in_inventory)))
        return names_of_item_in_inventory

    def OpenInventory(self):
        action = ""
        action_variants = [
            "экипировать предмет",
            "использовать предмет",
            "выйти"
        ]

        while action != "выйти":
            self.DisplayInventory()
            action = hepl_functions.validateAnswer(action_variants, False)
            
            if action == "экипировать предмет":
                class_of_weapons_can_equip = [
                    MeleeWeapon.__name__,
                    Shield.__name__,
                ]
                weapons = self.DisplayInventory(class_of_weapons_can_equip)
                choosen_weapon = hepl_functions.validateAnswer(weapons, False)

                self.equiped_weapon = self.GetItemByName(choosen_weapon)
                print(f"Вы эквипировали {self.equiped_weapon.name}")

                
    def GetItemByName(self, name_of_item: str):
        for item in self.inventory:
            if item.name == name_of_item:
                return item

class Enemy(Entity):
    def __init__(self, name: str, heath_points: int, attack_power: int):
        Entity.__init__(self, name, heath_points, attack_power)