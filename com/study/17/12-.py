#coding=utf-8
'''
Created on 2018年9月6日

@author: Pan
'''
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F("spam")
F("ham")
F("eggs")

G = tester(43)
G("spam")
G("ham")

F("bacon")


#边界情况
'''
def tester(start):
    def nested(label):
        state = 0
        nonlocal state
        print(label, state)
    return nested
'''

def tester(start):
    def nested(label):
        global state
        state = 0
        print(label, state)
    return nested

F = tester(0)
F('abc')
print(state)