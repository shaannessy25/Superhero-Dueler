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
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0
    def add_ability (self, ability):
        self.abilities.append(ability)
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)    

    def attack(self):
        damage_total = 0
        for ability in self.abilities:
            damage_total += ability.attack()
        return damage_total    

    def add_kill(self, num_kills):
        self.kills += num_kills
        return self.kills
    
    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        return self.deaths

    def defend(self):
        block_total = 0
        for armor in self.armors:
            block_total += armor.block()
        return block_total

    def take_damage(self, damage):
        self.current_health -= damage - self.defend()

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

            if self.is_alive() == False:
                self.add_deaths(1)
                opponent.add_kill(1)
                return print(f"{opponent.name} won!")
            else:
                self.add_kill(1)
                opponent.add_deaths(1)
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
                self.heroes.remove(hero)
                return self.heroes
        return 0

    def view_all_heroes(self):
        for heroes in self.heroes:
            print(heroes.name)

    def attack(self, other_team):
        hero1 = self.heroes[random.randint(0, (len(self.heroes))-1)]
        hero2 = other_team.heroes[random.randint(0, (len(other_team.heroes))-1)]
        hero1.fight(hero2)

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = health
            
        

    def stats(self):
        for hero in self.heroes:
            print(f" Hero: {hero.name} Kills: {hero.kills} Deaths: {hero.deaths} KD Ratio: {hero.kills/hero.deaths}")

class Arena:
    def __init__(self):
        self.team_one = Team('team_one')
        self.team_two = Team ('team_two')
    
    def create_ability(self):
        ability = input("Enter an ability: ")  
        attack_power = int(input("Enter number for attack power: "))
        return Ability(ability, attack_power)
    
    def create_weapon(self):
        weapon = input("Enter a weapon: ")
        attack_power = input("Enter number for attack power: ")
        return Weapon(weapon, attack_power)

    def create_armor(self):
        armor = input('Enter an armor: ')
        armor_power = input('Enter a number for armor power')
        return Armor(armor, armor_power)
    
    def create_hero(self):
        hero_name = input('Enter your hero name: ')
        hero = Hero(hero_name)
        ability = self.create_ability()
        weapon = self.create_weapon()
        armor = self.create_armor()
        hero.add_ability(ability)
        hero.add_weapon(weapon)
        hero.add_armor(armor)
        return Hero(hero_name)

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
    for count in range(30):
        winner = test_hero_fight()
        print(winner)