#coding=utf-8
'''
Created on 2018年10月19日

@author: Pan
'''
import math

def checkFlaotIsInt(value):
    checkValue = str(value)
    end = checkValue.split('.')[1:]
    for x in end:
        if x != '0': return False
        return True
    return False
    
i = 0
while (i <= 9999):
    plateNumber = "%04d" % i
    st = plateNumber[:2]
    end = plateNumber[2:]
    if st[:1] == st[1:] and end[:1] == end[1:] and st != end:
        x = math.sqrt(i)
        if checkFlaotIsInt(x):
            print (i)
    i += 1