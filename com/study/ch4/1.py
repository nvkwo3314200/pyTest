#coding=utf-8
'''
Created on 2018年9月4日
@author: Pan
'''

# hello world
print("hello world")
# 引入module
print('===== 引入module =====')
import sys
print(sys.platform)

# 变量
print('===== 变量 =====')
x = 1
y = 2

z = 3

z = x + y

y = z * y

# 数学模块
print('===== 数学模块  =====')
import math

print(math.pi)

print(math.sqrt(85))

x = 3.1415
print(x*2)

# 随机数模块
print('===== 随机数模块 =====')
import random

print(random.random())

print(random.choice([1,2,3,4,5,6,7,8,9,10]))

#字符串
print('===== 字符串 =====')
S = 'Spam'
print(len(S)) #表示字符串长度

print(S[0]) # 表示第一个元素

print(S[1]) # 表示第二个元素

print(S[-1]) #反向索引， 表示最后一个元素

print(S[-2]) #反向索引， 表示倒数第二个元素


print(S[1:3]) #字符分隔， 从下标1到下标3之间

print(S[0:5]) #字符分隔， 从下标1到下标3之间

print(S[:3]) #Spa

print(S[1:]) #pam

print(S[:]) #Spam

print(S[:-1]) #Spa

# 字符合并

print('Hello' + " " + "World!" )

# 重复
print("Hello " * 3)

try:
    S[0] = 'x' #error 数字， 字符， 元组 是不可变的
except Exception as e:
    print('Error:' , e);

S = 'x' + S[1:]
print(S)


print('===== 类型的特定方法 =====')
print(S.find('pa'))
print(S.replace('pa', 'XYZ'))
print(S)


line = 'aaaa, bbb,cc,ddd'
print(line.split(','))
print(line.upper())

line = '  aaaa, bbb,cc,ddd \n'
print(line.rstrip())
print(line.isalpha())

print('%s, eggs and %s' %('spam', 'SPAM'))

print('===== 寻求帮助  =====')
print(dir(S))

print(help(S.replace))

S = 'A\nB\tC'
print(S)
print(len(S))
print(ord('\n'))
S = 'A\0B\0C'
print(S)

msg = '''
    asdfasdf
    asdfsdf
    asdf
    asdf
    asdf
'''
print (msg)


import re
match = re.match('Hello[ \t]*(.*)world', 'Hello   Python world')
print(match.group(1))


L = [123, 'spam', 1.23]
print(len(L))
print(L[0])
print(L)
L = L + ['a',4, 'asdf']
print(L)
L.append('ADB')
print(L)
L.append(None)
print(L)
L.pop(2)
print(L)

M = ['aa', 'cc', 'bb']
print(M.sort())
print(M)
M.reverse()
print(M)

M = [[1,2,3], [4,5,6],[7,8,9]]
print(M[1][2])

col2 = [row[1] for row in M]
print(col2)

print([row[1] + 1 for row in M])

print([row[1] for row in M if row[1] % 2 == 0 ])

print([M[i][i] for i in [0,1,2]])

print([c*2 for c in 'spam'])

D = {'a' : 1, 'b':2, 'c':3}
Ks = list(D.keys())
print(Ks)
Ks.sort()
print(Ks)
for k in Ks :
    print(k , '-->' , str(D[k]))
    
for k in sorted(D) :
    print(k , '-->' , str(D[k]))
    
x = 4
while x > 0:
    print('Spam' * x)
    x -= 1
    print(x)
print (x)