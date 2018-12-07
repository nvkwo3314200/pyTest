#coding=utf-8
'''
Created on 2018年9月29日

@author: Pan
'''
import shelve
def printdb(db):
    for key in sorted(db):
        print(key , '\t==>', db[key])
db =  shelve.open('persondb')
printdb(db)
sue = db['Sue Jones']
print(sue)
sue.giveRaise(0.1)
db['Sue Jones'] = sue
printdb(db)
db.close()


