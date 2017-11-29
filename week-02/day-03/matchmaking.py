# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

max = 0
if len(girls) > len(boys):
    max = len(girls)
else:
    max = len(boys)

for i in range(max):
    if i < len(girls):
        order.append(girls[i])
    if i < len(boys):
        order.append(boys[i])
        
print(order)