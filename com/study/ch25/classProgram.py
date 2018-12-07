#coding=utf-8
'''
Created on 2018年9月29日

@author: Pan
'''

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)
        
if __name__ == '__main__':
    x = FirstClass();
    y = FirstClass();
    x.setdata('12345\'')
    y.setdata("pgf")
    x.display()
    y.display()
    x.data = 'New Data'
    x.display()