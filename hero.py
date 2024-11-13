from random import choice

# Hero with default "starting_health"
class Hero:
    def __init__(self, name, starting_health=100):
        # Name of our hero
        self.name = name
        #Starting health of our hero, which is 100
        self.starting_health = starting_health
        # Current health is always the same as their starting health when new hero is created
        # Meaning, no damage taken yet
        self.current_health = starting_health
    
    def __str__(self):
        return self.name
    
    #Current Hero will take turns fighting the opponent hero passed in
    # TODO: Stretch goal - include health as a determine of winner
    def fight(self, opponent):
        hero_fight = [self, opponent]
        winner = choice(hero_fight) 
        loser = opponent if winner == self else self
        print(f"{winner} defeats {loser}!")


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
