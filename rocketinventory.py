# This code prints a list of mugicians names by passing it to a function called
# show_rockets
print()
print ("DSR Labs Estes Rocket Launch Vehicle Fleet Inventory")
print()
def show_estesrocket(names):
    """Return a list of Estes low power rockets launch inventory"""
    for name in names:
        rocket_name = name.title()
        print(rocket_name)

rockets = ['1. Patriarch', '2. Dragonite', '3. Sizzler', '4. Shooting Star', '5. Skytrax', '6. Riptide', '7. Astrobeam']
show_estesrocket(rockets)
print()
