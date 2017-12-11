class Station(object):
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount
    
    def refill(self, car):
        self.gas_amount -= car.capacity - car.gas_amount
        car.gas_amount = 100

class Car(object):
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity

station = Station(5000)

car = Car()

print("Station gas amount: {}.".format(station.gas_amount))
print("Car gas amount: {}, capacity: {}.".format(car.gas_amount, car.capacity))

station.refill(car)

print("Station gas amount: {}.".format(station.gas_amount))
print("Car gas amount: {}, capacity: {}.".format(car.gas_amount, car.capacity))