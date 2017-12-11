class Animal(object):
    def __init__(self, hunger = 50, thirst = 50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1

dog = Animal()
cat = Animal(10, 20)

print("Dog hunger: {}, thirst: {}.".format(dog.hunger, dog.thirst))
print("Cat hunger: {}, thirst: {}.".format(cat.hunger, cat.thirst))

dog.eat()
dog.eat()
dog.drink()
cat.play()

print("Dog hunger: {}, thirst: {}.".format(dog.hunger, dog.thirst))
print("Cat hunger: {}, thirst: {}.".format(cat.hunger, cat.thirst))