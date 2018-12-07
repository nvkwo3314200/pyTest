#coding=utf-8
'''
Created on 2018年9月26日

@author: Pan
'''

def gensquares(N):
    for x in range(N):
        yield x ** 2
        
for x in gensquares(10):
    print(x, end = ":")