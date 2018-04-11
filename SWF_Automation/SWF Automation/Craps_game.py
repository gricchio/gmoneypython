'''
Created on Apr 11, 2018

@author: riccga
'''

from random import randint

bank = 60

point = 'off'
bet = 5 
odds = 3


def roll_dice():
    dice = randint(1,6)
    return dice



print "Bet is $" + str(bet) + " and that is backed up by " + str(odds) + "x odds!"

dicea = roll_dice()
diceb = roll_dice()
total = dicea + diceb


print "Dice A = " + str(dicea)
print "Dice B = " + str(diceb)
print "Total = " + str(total)
"""
if point =='off':
    if total == 7:
        print 'WIN'
    elif total == 2 or
"""