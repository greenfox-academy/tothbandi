from random import randint, randrange

class Randomize(object):
    def __init__(self):
        pass

    def d6(self):
        return randint(1, 6)

    def randlevel(self, act_level):
        level = act_level
        rand = randrange(100)
        if rand < 50:
            pass
        elif rand < 90:
            level += 1
        else:
            level += 2
        return level