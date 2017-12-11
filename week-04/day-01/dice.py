import random

class Dice(object):

    def __init__(self):
        self.dice = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(1,6)
        return self.dice

    def get_current(self, index=None):
        if index != None:
            return self.dice[index]
        else:
            return self.dice

    def reroll(self, index=None):
        if index != None:
            self.dice[index] = random.randint(1,6)
        else:
            self.roll()


dice = Dice()
print(dice.get_current())
dice.roll()
print(dice.get_current())
dice.reroll(3)
print(dice.get_current(3))
print(dice.get_current())

# Your task is to get where all dice is a 6

def all_dice_six(dice):
    print("The six dice are initally: ")
    print(dice.get_current())
    for i in range(len(dice.get_current())):
        while dice.get_current(i) != 6:
            dice.reroll(i)
    return dice.get_current()

dice = Dice()
dice.roll()
print("All the six dices are 6: ")
print(all_dice_six(dice))

