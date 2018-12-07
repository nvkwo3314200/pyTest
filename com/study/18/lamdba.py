#coding=utf-8
'''
Created on 2018年9月26日

@author: Pan
'''
from functools import reduce
print(reduce(lambda x, y : x + y, (1, 2,3,4,5)))
print(reduce(lambda x, y : x * y, (1, 2,3,4,5)))

def myreduce(function, seq):
    first = seq[0]
    for next in seq[1:]:
        first = function(first, next)
    return first

print(myreduce(lambda x, y : x + y, (1, 2,3,4,5)))
print(myreduce(lambda x, y : x * y, (1, 2,3,4,5)))

import operator, functools
x = functools.reduce(operator.add, (2, 3, 4))
print(x)

from b import spam
spam("a")