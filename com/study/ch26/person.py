'''
Created on 2018年9月29日

@author: Pan
'''
from classtools import  AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    '''    
    def __str__(self):
        return '[Person: %s, %s]'%(self.name, self.pay)
    '''
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    '''
    #bad way override super class's function
    if change happens to this function it means that hava to
    change two position to fix, 
    def giveRaise(self, percent, bonus=0.10):
        self.pay = int(self.pay * (1 + percent + bonus))
    '''
    #good way override supp class's function
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)
    
    def __getattr__(self, attr):
        return getattr(self, attr)        

class Department():
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(0.2)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    peak = Person("Peak Pan", pay=1000000)
    print(peak.name, peak.pay)
    
    print(peak.lastName())
    peak.giveRaise(0.1)
    print(peak.pay)
    print(peak)
    
    bob = Manager('Tom bob', pay = 1000000)
    bob.giveRaise(0.1)
    print(bob.pay)
    print(bob.__getattr__('pay'))
    
    king = Person('Ho King', pay= 1153684)
    
    java_department = Department(peak, bob)
    java_department.addMember(king)
    java_department.showAll()
    java_department.giveRaises(0.15)
    java_department.showAll()
