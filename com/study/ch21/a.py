#coding=utf-8
'''
Created on 2018年9月27日

@author: Pan
'''
from b import spam

import sys

# spam("hello")

print(list(sys.modules.keys()))

a = [x + "\n" for x in sys.path]
for x in sys.path:
    print(x, end = '\n')
    
