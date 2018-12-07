#coding=utf-8
'''
Created on 2018年9月5日

@author: Pan
'''

class Worker:
    '''
    classdocs
    '''


    def __init__(self, name, pay):
        '''
        Constructor
        '''
        self.name = name
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1 + percent)
        
        
        
bob = Worker('Bob Smith', 6000)

sue = Worker('Sue Jones', 8000)

print(bob.lastName())
bob.giveRaise(0.1)
print(bob.pay)
print(sue.lastName())
