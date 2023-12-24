import random


class Hat:
    def __init__(self):
        self.houses_1 = ["Gryffindor", "Hufflepuff", "Slytherin"]
    
    def sort_1(self, name):
        house = random.choice(self.houses_1)
        print(name, "is in", house)
    
    houses_2 = ["Gryffindor", "Hufflepuff", "Slytherin"]
    
    @classmethod
    def sort_2(cls, name):
        house = random.choice(cls.houses_2)
        print(name, "is in", house)
    
    
# hat = Hat()
# hat.sort_1("Harry")

Hat.sort_2("Harry")
