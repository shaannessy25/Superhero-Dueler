import random




class Ability:
    def __init__ (self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack (self):
        return random.randint(self.attack_strength, 100)
        


class Armor:
    def __init__ (self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block (self):
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

    def fight (self):
        pass

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Grace Hopper", 200, 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
