from aircraft import * 
from aircraft_carrier import * 

c1_ammo = 3000
c1_health = 2000
carrier1 = AircraftCarrier(c1_ammo, c1_health)

c2_ammo = 2500
c2_health = 5000
carrier2 = AircraftCarrier(c2_ammo, c2_health)

carrier1.add_aircraft('F35')
carrier1.add_aircraft('F16')
carrier1.add_aircraft('F16')
carrier1.add_aircraft('F35')

carrier2.add_aircraft('F35')
carrier2.add_aircraft('F16')
carrier2.add_aircraft('F35')
carrier2.add_aircraft('F16')
carrier2.add_aircraft('F35')
carrier2.add_aircraft('F16')
carrier2.add_aircraft('F35')


print(carrier1.get_status())
print(carrier2.get_status())






