from ability import Ability
import random

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)
        
    # Returns a random value between one half to the full
    # attack power of the weapon
    def attack(self):
        half_damage = self.max_damage // 2
        random_value = random.randint(half_damage, self.max_damage)
        return random_value
        
        

