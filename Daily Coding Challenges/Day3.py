'''
Created on Jun 17, 2017

@author: RiccGA
'''


def day_3(i):
    if i % 2 == 1:
        return "Weird"
    elif i % 2 == 0 and i <= 5 and i >= 2:
        return "Not Weird"
    elif i % 2 == 0 and i <= 20 and i >= 6:
        return "Weird"
    elif i % 2 == 0 and i > 20:
        return "Not Weird"
    else:
        return "Weird"


n = raw_input()
m = float(n)
print day_3(m)
