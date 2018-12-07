#coding=utf-8
'''
Created on 2018年11月23日

@author: Pan
'''
from operator import itemgetter

a_list = [(1, 'C'), (2, 'D'), (4, 'a'), (3, 'd'), (10, 'e'), (8, 'f')]
a_list.sort(key=itemgetter(1),reverse=False)
print(a_list)