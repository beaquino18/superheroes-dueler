from random import choice
from armor import Armor
from ability import Ability

# Hero class
class Hero:
    def __init__(self, name: str, starting_health: int = 100):
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        self.name = name
        #Starting health of our hero, which is 100
        self.starting_health = starting_health
        # Current health is always the same as their starting health when new hero is created
        # Meaning, no damage taken yet
        self.current_health = starting_health
    
    
    def add_ability(self, ability: Ability):
        self.abilities.append(ability)
    
    def add_armor(self, armor: Armor):
        self.armors.append(armor)
        
    #Calculate the total damage from all ability attacks
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    #Calculate the total block amount from all armor blocks
    def defend(self, incoming_damage: int):
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
    
    def is_alive(self):
        pass
    
    #Current Hero will take turns fighting the opponent hero passed in
    # TODO: Stretch goal - include health as a determine of winner
    def fight(self, opponent: 'Hero'):
        hero_fight = [self, opponent]
        winner = choice(hero_fight) 
        loser = opponent if winner == self else self
        print(f"{winner} defeats {loser}!")


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 70)
    hero.add_armor(shield)
    hero.take_damage(10)
    print(hero.current_health)
