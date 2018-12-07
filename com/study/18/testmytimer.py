#coding=utf-8
'''
Created on 2018年9月26日

@author: Pan
'''

import sys, mytimer

reps = 10000
repslist = range(reps)

# for 循环
def forloop():
    res = []
    for x in repslist:
        return res.append(x)
    return res 

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)

for test in (forloop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timecount(test)
    print ("-" * 33)
    print ('%-9s :%.5f =>' % (test.__name__, elapsed),  result)