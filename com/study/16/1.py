#coding=utf-8
'''
Created on 2018年9月6日

@author: Pan
'''

def times(x, y):
    "相乘"
    return x * y

#调用
print(times(3, 3.5))

# 多态
print(times('Ni', 3))


"""
    函数取交集
"""

def intersect(x, y):
    res = []
    for item in x:
        if item in y: res.append(item) 
    return res

print(intersect("spam", "sPan"))    

print([x for x in "spam" if x in "sPan"])

print(list(set("sPam") & set("span")))

print (intersect(["a", "b", "c", "c"], "Aasdf"))
        
