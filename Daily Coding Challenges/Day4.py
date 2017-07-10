'''
Created on Jul 10, 2017

@author: riccga
'''

age = raw_input()

class Person:
    def __init__(self,initialAge):
        if initialAge >= 0:
            self.age = initialAge
        else:
            print "Age is not valid, setting age to 0."
            self.age = 0
    def yearPasses(self):
        self.age += 1
    def amIOld(self):
        if self.age < 13:
            print "You are young."
        elif self.age >= 13 and self.age < 18:
            print "You are a teenager."
        else:
            print "You are old."