class Plant(object):
    def __init__(self, color, water_amount = 0.0):
        self.color = color
        self.water_amount = water_amount
    
    def watering(self, amount_of_water):
        self.water_amount += amount_of_water

    def needs_water(self):
        return self.water_amount < 20
