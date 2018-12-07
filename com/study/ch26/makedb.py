#coding=utf-8
'''
Created on 2018年9月29日

@author: Pan
'''
import shelve

import person
bob = person.Person('Bob Smith', pay = 12500)
sue = person.Person('Sue Jones', job='dev', pay=10000)
tom = person.Person('Tom Jones', pay = 20000)

import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()


db = shelve.open('persondb')
print(len(db))
print(list(db.keys()))
bob = db['Bob Smith']

help(bob)
print(bob.lastName())

for key in db:
    print(key, '==>', db[key])
    
for key in sorted(db):
    print(key, '==>', db[key])
db.close()