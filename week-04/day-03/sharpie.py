from random import random

class Sharpie(object):
    def __init__(self, color, width, ink_amount = 100.0):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount

    def use(self):
        self.ink_amount *= random()
        return self.ink_amount
    

# pen = Sharpie("green", 3.5)

# print("The pen color is {}, width is {} and the amount of the ink is {}.".format(
#     pen.color, pen.width, pen.ink_amount
# ))

# pen.use()

# print("The pen color is {}, width is {} and the amount of the ink is {}.".format(
#     pen.color, pen.width, pen.ink_amount
# ))