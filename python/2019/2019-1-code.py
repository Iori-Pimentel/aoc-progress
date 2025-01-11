data = open("inputs/2019-1.txt").read().splitlines()

def fuel_requirement(mass, recurse = False):
    if mass <= 0:
        return 0
    fuel = max(0, mass // 3 - 2)

    return fuel + (recurse and fuel_requirement(fuel, recurse))

rocket_fuel = [fuel_requirement(int(rocket_module)) for rocket_module in data]
all_fuel = [fuel_requirement(int(rocket_module), True) for rocket_module in data]
print(sum(rocket_fuel), sum(all_fuel))
