# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away

l = example.split(" ")
l.pop(2)
l.insert(2, "galaxy")
example = " ".join(l)

print(example)