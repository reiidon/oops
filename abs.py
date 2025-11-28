from abc import ABC, abstractmethod   #abtrst base class  
class Calc(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass
    
    @abstractmethod
    def mul(self):
        pass

    @abstractmethod
    def div(self):
        pass

   


class mycccc(Calc):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a // self.b

obj = mycccc(10, 5)
print( obj.add())
print( obj.sub())
print( obj.mul())
print( obj.div())