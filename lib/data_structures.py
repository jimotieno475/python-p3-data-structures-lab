spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names=[food['name'] for food in spicy_foods]
    return names
    pass

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spiciest=[food for food in spicy_foods if food['heat_level']>5]
    return spiciest
    pass

print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    cuisine=[food for food in spicy_foods if cuisine==food['cuisine']]
    return cuisine[0]
    pass

print (get_spicy_food_by_cuisine(spicy_foods, "American"))
print (get_spicy_food_by_cuisine(spicy_foods, "Thai"))


def print_spiciest_foods(spicy_foods):

    spiciest_list = get_spiciest_foods(spicy_foods)
    
    for food in spiciest_list:
        heat_level = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
    pass


print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    average=sum(food['heat_level'] for food in spicy_foods)
    return average/3
    pass

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicera= {    
            'name': 'Griot',
            'cuisine': 'Haitian',
           'heat_level': 10,
         }
    existing_food = [food for food in spicy_foods if spicy_food == food['name']]
    
    if not existing_food:
        # If the provided spicy_food doesn't exist, add spicera to the list
        spicy_foods.append(spicera)
    
    return spicy_foods
    pass
print(create_spicy_food(spicy_foods,"Griot"))