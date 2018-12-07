#coding=utf-8
'''
Created on 2018年9月5日

@author: Pan
'''
from _io import open

d = {'a': 1, 'b':2, 'c':3}

d['e'] = 99

print('f' in d)

if not 'f' in d:
    print('missing')

print(d.get('x', 0))

print(d['x'] if 'x' in d else 0)


f = open('data.txt', 'a', True, 'UTF-8')
f.write('Hello\n')
f.write('早上好\n')
f.close()

f = open('data.txt','r', True, 'UTF-8')
text = f.read()
print(text)
print(text.split())

X = set('spam')
Y = {'h', 'p', 'a'}
print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)

X = 3

print(X)

a = 3
b = a
a = 'spam'
print(a, b)

