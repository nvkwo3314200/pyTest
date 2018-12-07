#coding=utf-8
'''
Created on 2018年9月28日

@author: Pan
'''
X = 1
import time
from . import mod2
print(X, end=' ')
print(mod2.X, end=' ')
print(mod2.mod3.X)
for x in range(5):
    time.sleep(1)
    print('--------------',x,'----------------')
from imp import reload
reload(mod2)
#import mod2