class AirCraft(object):
    def __init__(self, ac_type, ammo = 0, max_ammo = 8, base_damage = 30):
        self.ac_type = ac_type
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        if self.ac_type == 'F35':
            self.max_ammo = 12
            self.base_damage = 50
        elif self.ac_type != 'F16' or self.ac_type != 'F35':
            print('No such an aircraft! :(')            
    
    def fight(self):
        damage_deals = self.ammo * self.base_damage
        self.ammo = 0
        return damage_deals

    def refill(self, ammos):
        free_space = self.max_ammo - self.ammo
        if ammos >= free_space:
            self.ammo = self.max_ammo
            return ammos - free_space
        else:
            self.ammo += ammos
            return 0
    
    def get_type(self):
        return self.ac_type

    def get_status(self):
        return 'Type {}, Ammo: {}, Base Damage: {}, All Damage: {}'.format(
                self.ac_type, self.ammo, self.base_damage, self.ammo * self.base_damage)
    

    
    # Type F35, Ammo: 10, Base Damage: 50, All Damage: 500


