import os
fuel = 0
total_fuel = 0

os.chdir(r'C:\Users\gino.ricchio\Desktop\Python Projects\Advent of Code')

list = []

with open('day1.txt') as f:
    listtxt = f.read().splitlines()

for text in listtxt:
    number = int(text)
    list.append(number)
    
print(list)

def fuel_per_item(item):
    fuel = 0
    fuel = (item / 3)//1 - 2
    print(str(fuel) + " is added by this item")
    return fuel

for x in list:
    print(str(total_fuel) + " Beginning Total Fuel")
    #fuel_per_item(x)
    total_fuel = total_fuel + fuel_per_item(x)
    print(str(total_fuel)  + " After adding this item")


print(total_fuel)
