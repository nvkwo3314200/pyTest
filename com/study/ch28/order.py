#coding=utf-8
'''
Created on 2018年9月30日

@author: Pan
'''

class Food:
    '''
        顾客买的东西
    '''
    def __init__(self, name): pass

class Lunch:
    '''
        一个容器和控制的类
    '''
    def __init__(self, customer): 
        self.customer = customer
    def order(self, name, foodName, employee):
        return self.customer.placeOrder(foodName, employee)
    def result(self): pass

class Customer:
    '''
            购买食物的顾客
    '''
    def __init__(self, name): 
        self.name = name
    def placeOrder(self, foodName, employee):
        print(employee)
        return employee.takeOrder(foodName)
    def printFood(self): pass

class Employee:
    '''
    顾客从他那里订餐
    '''
    def __init__(self, name):
        self.name = name
    def takeOrder(self, foodName): 
        print(' %s 卖出一份 %s ' % (self.name, foodName))
  
lzlm = Employee('兰州拉面')
tly = Employee('淘乐园')
sgby = Employee('三哥饼业')

lm = Food('拉面')
dxm = Food('刀削面')
gjf = Food('盖浇饭')
qcb = Food('千层饼')
kc = Food('快餐')    
pgf = Customer('Peak')

l = Lunch(pgf)
l.order('简单的中餐','拉面', lzlm)

 
    