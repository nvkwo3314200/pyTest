#coding=utf-8
'''
Created on 2018年9月26日

@author: Pan
'''

import time

resp = 1000
resplist = range(resp)

def timecount(func, *pargs, **kargs):
    start = time.clock()
    print(pargs, kargs)
    for x in resplist:
        ret = func()
    elapsed = time.clock() - start
    return (elapsed, ret)

def forloop():
    res = []
    for x in range(10000):
        return res.append(x)
    return res 

print(timecount(forloop))