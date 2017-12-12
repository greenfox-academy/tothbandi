from flower import Flower
from tree import Tree

class Garden(object):

    def __init__(self, plants = []):
        self.plants = plants

    def add_plant(self, plant):
        self.plants.append(plant)

    def watering(self, amount_of_water):
        print('Watering with {}'.format(amount_of_water))
        thirsties = 0
        for i in len(self.plants):
            if self.plants[i].needs_water:
                thirsties += 1
        amount_of_water /= thirsties
        for i in len(self.plants):
            if self.plants[i].needs_water:
                self.plants[i].watering(amount_of_water)
    

