'''
Created on 2018年9月29日

@author: Pan
'''

class rec(): pass
    

rec.name = '123'
rec.age = 456

x = rec()
y = rec()

def upperName(self):
        return self.name.upper()

print(x.name, ' ', y.name)
x.name = 'pgf'        
print(rec.name, ' ',x.name, ' ', y.name)

rec.method = upperName

print(x.method())
print(y.method())

