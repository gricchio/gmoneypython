'''
Created on Jul 10, 2017

@author: riccga
'''
n = raw_input()

for x in range(1, 11):
    answer = int(n) * x
    print str(n) + " x " + str(x) + " = " + str(answer)