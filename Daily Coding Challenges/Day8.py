'''
Created on Aug 31, 2017

@author: riccga
'''

num = int(raw_input())

phonebook = {}
x = 0
for i in range( 1, num+1):
        namenum = raw_input()
        sep = namenum.index(' ')
        name = namenum[0:sep]
        numsplit = namenum[sep+1:]
        x += 1
        phonebook[name] = numsplit
people = []

for i in range(1, num+1):
    contact = raw_input()
    people.append(contact)



for item in people:
        contacts = phonebook.keys()
        if item in contacts:
            lookingfor = contacts.index(item)
            print contacts[lookingfor] + '=' + phonebook[item]
        else:
            print 'Not found'
