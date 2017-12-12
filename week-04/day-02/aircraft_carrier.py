from aircraft import Aircraft 

class AircraftCarrier(Aircraft):
    def __init__(self, ammo, health, aircrafts = []):
        self.aircrafts = aircrafts
        self.ammo = ammo
        self.health = health

    def add_aircraft(self, ac_type):
        self.aircrafts.append(Aircraft(ac_type))

    def fill(self):
        if self.ammo == 0:
            raise ValueError('No ammos for fill :(')
        else:
            for aircraft in self.aircrafts:
                if self.ammo > 0 and aircraft.get_type() == 'F35':
                    self.ammo = aircraft.refill(self.ammo)
            for aircraft in self.aircrafts:
                if self.ammo > 0:
                    self.ammo = aircraft.refill(self.ammo)

    def fight(self, another):
        damage_deals = 0
        for aircraft in self.aircrafts:
            damage_deals += aircraft.fight()
        another.health -= damage_deals

    def get_status(self):
        damage_deals = 0
        for aircraft in self.aircrafts:
            damage_deals += aircraft.fight()
        status = 'HP: {}, Aircraft count: {}, Ammo Storage: {}, Total damage: {}\n'.format(
            self.health, len(self.aircrafts), self.ammo, damage_deals)
        status += 'Aircrafts:\n'
        for aircraft in self.aircrafts:
            status += aircraft.get_status()
        return status





