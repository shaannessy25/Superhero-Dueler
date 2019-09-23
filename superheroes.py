import random




class Ability:
    def __init__ (self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack (self):
        strength = random.randint(self.attack_strength, 100)
        return strength


class Armor:
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block (self, max_block):
        block = random.randint(0, self.max_block)
        return block

class Hero:
    def __init__ (self, name, starting_health, current_health):
        self.name = name
        self.starting_health = starting_health
        self.current_health = current_health
        self.abilities = list()
        self.armors = list()

    def add_ability (self, ability):
        self.abilities.append(ability)
    def attack (self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total    

    def defend (self, damage_amt):
        block_total = 0
        for armor in self.armors:
            block_total += armor.block()
        return block_total

    def add_armor (self, armor):
        self.armors.append(armor)    

    def take_damage (self):
        pass
    def is_alive (self):
        pass
    def fight (self):
        pass

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200, 50)
    hero.add_armor(armor)
    print(hero.add_armor())