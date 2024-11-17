from hero import Hero
import random

class Team():
    # Initialize team with team name and empty list of heroes
    def __init__(self, name: str):
        self.name = name
        self.heroes = list()
    
    # Add hero object to self.heroes
    def add_hero(self, hero:Hero):
        self.heroes.append(hero)
    
    # Remove a hero from heroes list. If Hero isn't found, return 0
    def remove_hero(self, name:str):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
            
        if not foundHero:
            return 0
    
    # Prints out all heroes to the console
    def view_all_heroes(self):
        for hero in self.heroes:
            print(f"{hero.name}")

    #Pring team statistics
    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                kd = hero.kills
            else:
                kd = hero.kills / self.deaths
            
            print(f"{hero.name} Kill/Deaths:{kd}")
            
    #Reset all heroes health to starting_health
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
    
    #Battle each team against each other
    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()
        
        for hero in self.heroes:
            living_heroes.append(hero)
            
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            #Randomly select heroes from both team
            hero_choice = random.choice(living_heroes)
            opponent_choice = random.choice(living_opponents)
            
            #Heroes fight
            hero_choice.fight(opponent_choice)
            
            if not hero_choice.is_alive():
                living_heroes.remove(hero_choice)
            
            if not opponent_choice.is_alive():
                living_opponents.remove(opponent_choice)
            
        self.stats()
        other_team.stats()


