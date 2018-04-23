'''
Created on Apr 11, 2018

@author: riccga
'''

from random import randint

sbank = 60
bank = sbank

point = 'off'
bet = 5 
odds = 0

def roll_dice():
    dice = randint(1,6)
    return dice

bank = bank - bet

print bank

print "Bet is $" + str(bet)

dicea = roll_dice()
diceb = roll_dice()
total = dicea + diceb


print "Dice A = " + str(dicea)
print "Dice B = " + str(diceb)
print "Total = " + str(total)


if point =='off':
    if total == 7:
        print 'WIN'
        bank = bank + bet*2
        print bank
    elif total == 2 or total == 12:
        print 'LOSE'
    else:
        point = "on"
        point_num = total
        print "Point is on " + str(total)
        print "How much odds would you like to put on it?"
        odds = float(raw_input())
        bank = bank - odds*bet
      
while point != 'off':
    dicea = roll_dice()
    diceb = roll_dice()
    total = dicea + diceb
    print "Dice A = " + str(dicea)
    print "Dice B = " + str(diceb)
    print "Total = " + str(total)
    if total == point_num:
        point = 'off'
        bank = float(bank) + float(bet)*2 + float(bet)*odds*2.5
        break
    elif total == 7:
        point = 'off'
        break

print 'You have made ' + str(float(bank-sbank)) + 'Dollars ' + ' or a ' + str(float((bank-sbank)/sbank*100)) + str(' percent!')