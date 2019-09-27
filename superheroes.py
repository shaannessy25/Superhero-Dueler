import random


class Ability:
    def __init__ (self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack (self):
        return random.randint(0, self.attack_strength)
        
class Weapon(Ability):
    def attack(self):
        return random.randint(self.attack_strength // 2, self.attack_strength)

class Armor:
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block (self):
        block = random.randint(0, self.max_block)
        return block

class Hero:
    def __init__ (self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = 100
        self.abilities = list()
        self.armors = list()

    def add_ability (self, ability):
        self.abilities.append(ability)

    def attack (self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total    

    def defend (self):
        block_total = 0
        for armor in self.armors:
            block_total += armor.block()
        return block_total

    def add_armor (self, armor):
        self.armors.append(armor)    

    def take_damage (self, damage):
        self.current_health -= damage - self.defend()

    def is_alive (self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight (self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities):
            return print("Draw!")
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.is_alive() == False:
            return print(f"{opponent.name} won!")
        else:
            return print(f"{self.name} won!")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, name):
        self.heroes.append(name)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(name)
                return self.heroes
        return 0

    def view_heroes(self):
        for heroes in self.heroes:
            print(heroes.name)

def test_hero_fight():
    hero1 = Hero("Wonder Woman", 200)
    ability1 = Ability("Super Speed", 30)
    ability2 = Ability("Super Eyes", 130)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)

    hero2 = Hero("Dumbledore", 200)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)
    if hero1.is_alive():
        return hero1.name
    elif hero2.is_alive():
        return hero2.name
    else:
        return 'tie'

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    for count in range(2):
        winner = test_hero_fight()
        print(winner)