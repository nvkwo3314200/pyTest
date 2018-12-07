#coding=utf-8
'''
Created on 2018年9月29日

@author: Pan
'''
print('I am ' , __name__)
def minmax(test, *args):
    res = args[0]
    for arg in args:
        res = test(res, arg)
    return res

def min(x, y): return x if x < y else y
def max(x, y): return x if x > y else y


if __name__ == '__main__':
    print(minmax(min, 1, 2,3,4,5,6,7))
    print(minmax(max, 1, 2,3,4,5,6,7))    