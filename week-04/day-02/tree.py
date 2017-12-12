from plant import Plant

class Tree(Plant):
    def __init__(self, color, water_amount = 0.0):
        super().__init__((self, color, water_amount))
    
    def watering(self, amount_of_water):
        self.water_amount += amount_of_water * 0.4

    def needs_water(self):
        return self.water_amount < 10

    def __repr__(self):
        intro = 'The {} Tree '.format(self.color)
        if self.needs_water():
            intro += 'needs water'
        else:
            intro += 'doesnt need water' 