#coding=utf-8

'''
    lambda 表达式
    lambda 表达式起到了一种函数速写的作用， 你总是可以用def 来改写它，但是使用lambda会使代码看起来更简洁
'''

L = [lambda x:x*2,
     lambda x:x*3,
     lambda x:x*4
    ]

for x in L:
    print(x(4))


print(L[1](4))

lower = lambda x, y : x if x < y else y

print(lower('aa', 'bb'))
print(lower('bb', '11'))


''' 
    lambda 嵌套循环
'''
import sys
showlist = lambda x: list(map(sys.stdout.write, x))
showlist({'spam\n', 'api\n', 'doc\n', 'jetty\n'})

''' 
         嵌套lambda和作用域 
'''
def action(x):
    return (lambda y: x * y)
act = action(9)
act2 = action(1)
print(act(2))
print(act(3))
print(act2(2))
print(act2(3))


''' 
    lambda回调
'''
import sys
from tkinter import Button, mainloop
x = Button(text = 'Press Me',
           command = (lambda:sys.stdout.write('Spam\n'))
           )
x.pack()
mainloop()