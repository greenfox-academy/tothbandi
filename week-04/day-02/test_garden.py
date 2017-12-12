from flower import Flower
from tree import Tree
from garden import Garden 

garden = Garden()

garden.add_plant(Flower('yellow'))
garden.add_plant(Flower('blue'))
garden.add_plant(Tree('purple'))
garden.add_plant(Tree('orange'))

for i in range(len(garden.plants)):
    print(garden.plants[i])

print()

garden.watering(40)

for i in range(len(garden.plants)):
    print(garden.plants[i])

print()

garden.watering(70)

for i in range(len(garden.plants)):
    print(garden.plants[i])
