from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    
    @abstractmethod    
    def action(self):
        pass
    
    
class Sub(Super):
    def action(self):
        print('spam')      
    pass
    
if __name__ == '__main__':
    X = Sub()
    X.delegate()