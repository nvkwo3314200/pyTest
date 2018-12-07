#coding=utf-8
'''
Created on 2018年10月15日

@author: Pan
'''


f = open('中华.txt','w', encoding='utf-8')
f.write(u"hello 高峰\n")
f.close()

fr = open('中华.txt', 'r', encoding='utf-8')
print(fr.readlines());

a = u'asdf中华小当家'
print(a)
