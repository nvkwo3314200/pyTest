#coding=utf-8
'''
Created on 2018年9月29日

@author: Pan
'''
X = 11

def f():
    print(X)
    
def g():
    X = 22
    print(X)
    
class C:
    X = 33
    def m(self):
        X = 44
        self.X = 55
        
if __name__ == '__main__':
    print(X)
    f();
    g();
    c = C();
    print(C.X)
    print(c.X)
    c.m()
    print(C.X)
    print(c.X)
    