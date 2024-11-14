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
            
        fighting = True    
        while fighting:
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
            
            if opponent.current_health <= 0:
                print(f"{self.name} won")
                break
            elif self.current_health <= 0:
                print(f"{opponent.name} won")
                break

            fighting = False
    
    #use while loop
    #take into account the possibility that both heroes may not have abilities and
    #   therefore will do no damage
    #   use if statement and check to see if at least one hero has an ability.
    #   if no abilities exist, print out "Draw"
    # When a hero wins, print "HEroName won"
    
    # calculate all hero attacks, and then opponent take damage


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
