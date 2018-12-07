#coding=utf-8
'''
Created on 2018年9月30日

@author: Pan
'''
class Spam:
    numberInstances = 0
    def __init__(self):
        Spam.numberInstances += 1
    
    @staticmethod
    def printNumberInstance():
        print('Number of instances created: ', Spam.numberInstances)
        
x = Spam()
y = Spam()
z = Spam()
Spam.printNumberInstance()


# extend
class Adder:
    def __init__(self, data):
        self.data = data
    def add(self, x, y):
        print('Not Implemented')
        
    def __add__(self, y):
        return self.add(self.data, y.data)

class ListAdder(Adder):
    def add(self, x ,y):
        return list(set(x) | set(y))
    
class DictAdder(Adder):
    def add(self, x ,y):
        for key,value in y.items():
            if x.__contains__(key):
                x[key] = [x[key],value]
            else:
                x[key] = value    
        return x
    
l = ListAdder([1,2,3,4])
m = ListAdder([1,4,6,7])
y = DictAdder({'a':1, 'b':2})
z = DictAdder({'c':3, 'b':(3,33)})
print(y + z)
print(l + m)