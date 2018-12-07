#coding=utf-8
from mimetypes import init

class Person:
    def __init__(self, name):
        self._name = name
    
    def getName(self):
        print('fetch...')
        return self._name
    
    def setName(self, name):
        print('change...')
        self._name = name
        
    def delName(self):
        print('delete...')
        del self._name
    
    name = property(getName, setName, delName, 'name properties doc')
    
bob = Person('Bob Smith')
print(bob.name)
bob.name = 'Robert Smith'
print(bob.name)
del bob.name

print('-' * 20)
sue = Person('Sue Jones')
print(sue.name)
print(Person.name.__doc__)