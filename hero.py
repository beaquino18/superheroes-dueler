from random import choice
from armor import Armor
from ability import Ability
from weapon import Weapon

# Hero class
class Hero:
    def __init__(self, name: str, starting_health: int = 100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    
    def add_ability(self, ability: Ability):
        self.abilities.append(ability)
    
    def add_armor(self, armor: Armor):
        self.armors.append(armor)
        
    # Add weapon to self.abilities    
    def add_weapon(self, weapon: Weapon):
        self.abilities.append(weapon)
        
    # Update self.kills by num_kills amount
    def add_kill(self, num_kills):
        self.kills += num_kills
    
    #Update deaths with num_deaths
    def add_death(self, num_deaths):
        self.deaths += num_deaths
        
    #Calculate the total damage from all ability attacks
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    #Calculate the total block amount from all armor blocks
    def defend(self, damage):
        #Check if hero is dead (0 health)
        if self.current_health <= 0:
            return 0
        
        # Check if there are no armors
        if len(self.armors) == 0:
            return 0
        
        # Calculate total block from all armors
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    #Updates self.current_health to reflect the damage minus the defense
    def take_damage(self, damage: int):
        total_defense = self.defend(damage)
        total_damage = damage - total_defense
        
        if total_damage <= 0:
            print(f"{self.name} completely blocked the attack")
            return
        
        self.current_health -= total_damage
    
    #Return true or false depending on whether the hero is alive or not
    def is_alive(self):
        if self.current_health <= 0:
            return False
        
        return True
    
    #Current Hero will take turns fighting the opponent hero passed in
    def fight(self, opponent: 'Hero'):
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
            return
            
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            
            if not opponent.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} won")
                return
            
            if not self.is_alive():
                opponent.add_kill(1)
                self.add_death(1)
                print(f"{opponent.name} won")
                return



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

