#coding=utf-8
'''
Created on 2018年9月30日

@author: Pan
'''

class Mylist(list):
    #初始化
    '''
             为什么拷贝初始值很重要
    '''
    def __init__(self, data):
        if isinstance(data, list): 
            self.data = data[:]
        else:
            self.data = [data]    
        
    # +
    def __add__(self, y): pass
    # 索引
    def __getitem__(self): pass
    def __setitem__(self): pass
    def __delitem__(self): pass
    # 长度
    def __len__(self): pass
    #子集
    def __sub__(self): pass 
    # 迭代
    def __iter__(self): pass
    def __next__(self): pass
    
    #成员关系
    def __contains__(self): pass
    
    
class MylistSub(Mylist):
    