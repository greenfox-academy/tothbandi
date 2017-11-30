# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def print_separator(columns_width):
    for i in range(len(columns_width)):
        print("+", end='')
        for j in range(columns_width[i]):
            print("-", end='')
    print("+")

def print_line(str1, str2, str3, columns_width):
    print("| ", end='')
    print(str1, end='')
    for i in range(columns_width[0] - len(str1) - 1):
        print(" ", end='')
    print("| ", end='')
    print(str2, end='')
    for i in range(columns_width[1] - len(str2) - 1):
        print(" ", end='')
    print("| ", end='')
    print(str3, end='')
    for i in range(columns_width[2] - len(str3) - 1):
        print(" ", end='')
    print("|")



def table(alc_list):
    columns_width = [0, 0, 0]
    for an_item in alc_list:
        if len(an_item['name']) > columns_width[0]:
            columns_width[0] = len(an_item['name'])
    columns_width[0] += 2
    columns_width[1] = len("Needs cooling") + 2
    columns_width[2] = len("In stock") + 2
    print_separator(columns_width)
    print_line("Ingredient", "Needs cooling", "In stock", columns_width)    
    print_separator(columns_width)    
    for item in ingredients:
        str1 = item['name']
        if item['needs_cooling']:
            str2 = "Yes"
        else:
            str2 = "No"
        if item['in_stock'] == 0:
            str3 = "-"
        else:
            str3 = str(item['in_stock'])
        print_line(str1, str2, str3, columns_width)



    print_separator(columns_width)    



table(ingredients)
