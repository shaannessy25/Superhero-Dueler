import random




class Ability:
    def __init__ (self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack (self):
        return random.randint(0, self.attack_strength)
        


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

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman", 200)
    hero2 = Hero("Dumbledore", 200)
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

