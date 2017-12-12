
class Flower():
    def __init__(self, color, water_amount = 0.0):
        self.color = color
        self.water_amount = water_amount
    
    def watering(self, amount_of_water):
        self.water_amount += amount_of_water * 0.75

    def needs_water(self):
        return self.water_amount < 5

    def __str__(self):
        intro = 'The {} Flower '.format(self.color)
        if self.needs_water():
            intro += 'needs water'
        else:
            intro += 'doesnt need water'
        return intro

