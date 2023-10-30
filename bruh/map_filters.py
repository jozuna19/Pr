menu = ["espresso", "mocha", "latte",
        "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

"""A map allows you to take all objects in a list
and applies a function
"""
# map_coffee = map(find_coffee, menu)
# print(map_coffee)

# for x in map_coffee:
#     print(x)


""""
A filter does the same thing a map does, but takes
the results and creates a new list with only true values
"""
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)