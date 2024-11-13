class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
        
    def bark(self):
        print("Woof!")
        
    def sits(self):
        return "sit"
        
    def roll_over(self):
        return "roll over"


