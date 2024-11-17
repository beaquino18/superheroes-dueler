from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
    
    #Prompt for ability information
    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        
        return Ability(name, max_damage)
    
    #Prompt user for Weapon information
    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")
        
        return Weapon(name, max_damage)
    
    #Prompt user for Armor information
    def create_armor(self):
        name = input("What is the armor name? ")
        max_block = input("What is the max block of the armor? ")
        
        return Armor(name, max_block)
    
    #Prompt user for Hero information
    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
            
        return hero
    
    
    #Prompt user to build team_one
    def build_team_one(self):
        team_name = input("What is the name of Team One?  ")
        self.team_one = Team(team_name)
        num_heroes = int(input("How many members would you like on Team One?\n"))
        for i in range(num_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
            
    #Prompt user to build team_two
    def build_team_two(self):
        team_name = input("What is the name of Team Two?  ")
        self.team_two = Team(team_name)
        num_team_members = int(input("How many members would you like on Team Two?\n"))
        for i in range(num_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    #Battle team_one and team_two together
    def team_battle(self):
        self.team_one.attack(self.team_two)
        
    
    #Calculate the average K/D for team one
    def average_kd_team1(self):
        team_kills = 0
        team_deaths = 0
        
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        
        if team_deaths == 0:
            team_deaths = 1
        print(f"{self.team_one.name} average K/D was: {str(team_kills/team_deaths)}")
        
    
    def average_kd_team2(self):
        team_kills = 0
        team_deaths = 0
        
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        
        if team_deaths == 0:
            team_deaths = 1
        print(f"{self.team_two.name} average K/D was: {str(team_kills/team_deaths)}")
    
    def survive_team1(self):
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print(f"survived from {self.team_one.name} : {hero.name}")
                
    def survive_team2(self):
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(f"survived from {self.team_two.name} : {hero.name}")
    
        
    #Print team stats to terminal
    def show_stats(self):
        print(f"\n {self.team_one.name} statistics: ")
        self.team_one.stats()
        print(f"\n {self.team_two.name} statistics: ")
        self.team_two.stats()
        print("\n")
        
        # Print verage KD of both teams
        self.average_kd_team1()
        self.average_kd_team2()
        
        # Show all survived heroes in each team
        self.survive_team1()
        self.survive_team2()


if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
