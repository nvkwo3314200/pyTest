#coding=utf-8
'''
    test iterator
    test python
    test import
'''

f = open("__init__.py", 'r', True, 'utf-8')
'''
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

print(f.__next__() )
print(f.__next__() )
print(f.__next__() )
print(f.__next__() )
print(f.__next__() )
print(f.__next__() )
print(f.__next__() )
'''

'''
while True:
    char = f.read(1)
    if not char: break
    print(char)

for char in f.read():
    print(char)
'''
while True:
    char = f.readline()
    if not char: break
    print(char)

f.close()

f = open("__init__.py", 'rb')
while True:
    chunk = f.read(10)
    if not chunk: break
    print(chunk)
f.close()


L = [1, 2, 3]

I = iter(L)
'''
print(next(I))
print(next(I))
print(next(I))
'''
while True:
    try:
        X = next(I)
    except Exception:
        break
    print(X ** 2)
    
import os
P = os.popen('dir')
print(P.__next__())

while True:
    try:
        print(P.__next__())
    except Exception:
        break


R = range(-3, 3)
R1 = range(9, 15)
print(list(R))
print(list(zip(R, R1)))

L = list(range(1, 6))
L = [x + 10 for x in L]
print(L)

lines = [x.rstrip() for x in open("__init__.py") if 'print' in x ]
for x in lines:
    print(x)  
      
c = R
print(list(map(ord, ['a','b', 'c'])))
