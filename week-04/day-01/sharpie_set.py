from random import random

class Sharpie(object):
    def __init__(self, color, width, ink_amount = 100.0):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount *= random()

    def count_usable(self):
        return self.ink_amount > 10.0

    def __repr__(self):
        return "(" + self.color + ", " + str(self.width) + ", " + str(self.ink_amount) + ")"

class SharpieSet(object):
    def __init__(self, sharpies = []):
        self.sharpies = sharpies
    
    def add(self, sharpie):
        self.sharpies.append(sharpie)
    
    def remove_trash(self):
        i = len(self.sharpies)
        while i > 0:
            i -= 1
            if not self.sharpies[i].count_usable():
                self.sharpies.pop(i)

    def __repr__(self):
        return str(self.sharpies)

s1 = Sharpie("red", 0.5)
s2 = Sharpie("green", 0.7)
s3 = Sharpie("blue", 1.0)
s4 = Sharpie("black", 2.0)

sharpies = SharpieSet()
sharpies.add(s1)
sharpies.add(s2)
sharpies.add(s3)
sharpies.add(s4)

print(sharpies)

s1.use()
s1.use()
s1.use()
s1.use()
s4.use()
s4.use()
s4.use()
s4.use()

print(sharpies)

sharpies.sharpies[0].use()

print(sharpies)

sharpies.remove_trash()

print(sharpies)

