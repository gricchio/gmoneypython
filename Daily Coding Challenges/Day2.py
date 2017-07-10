'''
Created on Jun 17, 2017

@author: RiccGA
'''

i1 = raw_input()
i2 = raw_input()
i3 = raw_input()


mealCost = float(i1)
tipPercent = float(i2)/100
taxPercent = float(i3)/100

def day_2(a,b,c):
    pretax = a
    tip = float(a * b)
    tax = float(a * c)
    total_meal = pretax + tip + tax
    return round(total_meal,0)

ttl = str(day_2(mealCost,tipPercent,taxPercent))

words1 = "The total meal cost is "
words2 = " dollars."

print  words1 + ttl + words2