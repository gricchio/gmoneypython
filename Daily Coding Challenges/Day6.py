'''
Created on Jul 10, 2017

@author: riccga
'''
#test cases
T = int(raw_input())



for i in range(0,T):
    first = []
    last = []
    string = raw_input()
    for j in range(0, len(string)):
        if j % 2 == 0:
            first.append(string[j])
        
    for j in range(0, len(string)):
        if j % 2 != 0:
            last.append(string[j])

    first_str = ''.join(x.strip() for x in first)
    last_str = ''.join(x.strip() for x in last)
    print str(first_str) + " " + str(last_str)

    




