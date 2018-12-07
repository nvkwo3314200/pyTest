#coding=utf-8
'''
Created on 2018年9月29日

@author: Pan
'''

from classProgram import FirstClass

class SecondClass(FirstClass):
    data = 43
    def display(self):
        print('Current value = "%s"' % self.data)
        
   
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    
    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data
    
    def mul(self, other):
        self.data *= other
        
        
if __name__ == '__main__':
   z = SecondClass()
   z.setdata(42)
   z.display() 
   
   a = ThirdClass('abc')
   a.display()
   
   print(a)
   
   b = a + 'xyz'
   
   b.display()
   
   a.mul(3)
   print(a)