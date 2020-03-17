

fuel = 0
total_fuel = 0
fff = []
fff_extra = 0
ttl_fuel = 0
list = []

def sum_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum

with open('C:\Users\gino.ricchio\Documents\Python Materials\day1data.txt') as f:
    listtxt = f.read().splitlines()

for text in listtxt:
    number = int(text)
    list.append(number)
    
print list

def fuel_per_item(item):
    fuel = 0
    fuel = (item / 3)//1 - 2
    print str(fuel) + " is added by this item"
    if fuel < 0:
        return 0
    else: return fuel


for x in list:
    print str(total_fuel) + " Beginning Total Fuel"
    total_fuel += fuel_per_item(x)
    fff.append(fuel_per_item(x))

print str(total_fuel) + " Ending Fuel Before Fuel Calcs"


while sum_list(fff) > 0:
    new_list = []
    global ttl_fuel
    for y in fff:
        ttl_fuel += fuel_per_item(y)
        new_list.append(fuel_per_item(y))
        print ttl_fuel
    fff = new_list
    print fff
    print ttl_fuel

grandsum = ttl_fuel + total_fuel

print grandsum