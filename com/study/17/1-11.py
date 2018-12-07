#coding=utf-8
'''
Created on 2018年9月6日

@author: Pan
'''

# Global scope
X = 99
def func(Y):
    #local scope
    Z = X + Y
    return Z

print(X)
print(func(20))

#内置作用域
import builtins
print(dir(builtins))

# zip 是内置函数，现在定义此函数将覆盖
def zip(x,y):
    return x + y;

r = zip((1,2,3,4), (5,6,7))
print(r)


# Global 语句
X = 88
def func():
    global X #去掉后结果会变成不能改变模块内X的值 
    X = 99

func()
print(X)

y, z = 1, 2
def all_global():
    global x
    x = y + z

all_global()
print(x)

import first
print(first.X)
first.X = 200
print(first.X)

X = 99
def f1():
    X = 88
    def f2():
        print(X)
    f2()
f1()


def f1():
    X = 88
    def f2():
        print(X)
    return f2
action = f1()
action()


def maker(N):
    def action(X):
        return X ** N
    return action
f = maker(2)
print(f)

print(f(3))
print(f(4))

def func():
    x = 4
    action = (lambda n: x ** n)
    return action

x = func()

print(x(3))

a = (lambda n: 3 ** n)
print(a(2))

print(list(range(5)))

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = makeActions()

print([ f(2) for f in acts])


