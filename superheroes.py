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
        kd = 0
        total_kills = 0
        total_deaths = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        if total_deaths == 0:
            kd = total_kills
        else:
            kd = total_kills/total_deaths
        return kd

class Arena:
    def __init__(self):
        self.team1 = Team('team 1')
        self.team2 = Team ('team 2')
    
    def create_ability(self):
        ability = input("Enter an ability: ")  
        attack_power = int(input("Enter number for attack power: "))
        return Ability(ability, attack_power)
    
    def create_weapon(self):
        weapon = input("Enter a weapon: ")
        attack_power = int(input("Enter number for attack power: "))
        return Weapon(weapon, attack_power)

    def create_armor(self):
        armor = input('Enter an armor: ')
        block_power = int(input('Enter a number for armor power: '))
        return Armor(armor, block_power)
    
    def create_hero(self):
        name = input("Enter a Hero name: ")
        new_Hero = Hero(name, starting_health=100)
        want_ability = input("Do you want an ability? Y or N:  ")
        want_weapon = input("Do you want a weapon? Y or N:  ")
        want_armor = input("Do you want armor? Y or N:  ")
        if want_ability == "Y" or want_ability == 'y':
            new_Hero.add_ability(self.create_ability())
        if want_weapon == "Y" or want_weapon == 'y':
            new_Hero.add_weapon(self.create_weapon())
        if want_armor == "Y" or want_armor == 'y':
            new_Hero.add_armor(self.create_armor())
        return new_Hero

    
    def build_team_one(self):
        team_name = input('Enter your team\'s name: ')
        team1 = Team(team_name)
        fighters = int(input("Enter a number of heros you wish to play for: "))
        
        for i in range(fighters):
            hero = self.create_hero()
            team1.add_hero(hero)
        self.team1 = team1

    def build_team_two(self):
        team_name = input('Enter your opponent\'s team\'s name: ')
        team2 = Team(team_name)    
        players = int(input('Enter a number of heros you wish to play for: '))

        for i in range(players):
            hero = self.create_hero()
            team2.add_hero(hero)
        self.team2 = team2
    def team_battle(self):
        self.team1.attack(self.team2)

    def team_deaths(self, teamAlive):
        teamDeaths = 0
        for hero in teamAlive:
            if hero.current_health == 0:
                teamDeaths += 1
        if teamDeaths == len(teamAlive):
            return True
        else:
            return False

    def show_stats(self):
        team1 = self.team_deaths(self.team1.heroes)
        team2 = self.team_deaths(self.team2.heroes)        
        
        if team1 == False:
            print(f"The winner is {self.team1.name}")
            print("The Survivors are: ")
            for hero in self.team1.heroes:
                if hero.is_alive():
                    print(hero.name)
        elif team2 == False:
            print(f"Victor is Team {self.team2.name}")
            print("The Survivors are: ")
            for hero in self.team2.heroes:
                if hero.is_alive():
                    print(hero.name)
                else:
                    print("None bro, all my friends are dead")
        elif team1 == False and team2 == False:
            print("DRAW!")

        print(f'Team One KDR: {self.team1.stats()}')
        print(f'Team Two KDR: {self.team2.stats()}')


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
    # for count in range(30):
    #     winner = test_hero_fight()
    #     print(winner)
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team1.revive_heroes()
            arena.team2.revive_heroes()