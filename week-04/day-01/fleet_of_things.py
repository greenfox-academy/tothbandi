from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch


thing1 = Thing("Get milk")
thing2 = Thing("Remove the obstacles")
thing3 = Thing("Stand up")
thing3.complete()
thing4 = Thing("Eat lunch")
thing4.complete()

fleet.add(thing1)
fleet.add(thing2)
fleet.add(thing3)
fleet.add(thing4)

print(fleet)