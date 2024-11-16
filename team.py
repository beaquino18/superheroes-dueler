from hero import Hero

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
