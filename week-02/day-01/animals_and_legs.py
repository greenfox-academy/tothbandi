# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have
chicken = int(input("The number of the chickens in the farm: "))
pig = int(input("The number of the pigs in the farm: "))
print("The number of animal legs in the farm: " + str(chicken * 2 + pig * 4))