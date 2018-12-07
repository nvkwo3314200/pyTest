#coding=utf-8
'''
Created on 2018年9月30日

@author: Pan
'''

def count(aClass):
    aClass.numberInstances = 0
    return aClass

@count
class Spam: pass

@count
class Sub(Spam): pass

@count
class Other(Spam): pass

#print(Other.numberInstances)



class X:pass

class Y:pass

X.a = 1
Y.b = 2
X.c = 3
Y.a = X.a + Y.b + X.c

for X.i in range(Y.a): print(X.i)

print (X.i)