
watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival


print("Queue of festivalgoers: ")
print(queue)

def security_check(queue_for_enter):
    l = []
    global security_alcohol_loot
    for person in queue_for_enter:
        if person['guns'] > 0:
            watchlist.append(person['name'])
            security_alcohol_loot += person['alcohol']
        else:
            if person['alcohol'] > 0:
                security_alcohol_loot += person['alcohol']
                person['alcohol'] = 0
            l.append(person)
    return l


print("Goers let enter: ")
print(security_check(queue))

print("Watchlist because of gun: ")
print(watchlist)

print("Confiscated alcohol: " + str(security_alcohol_loot))

