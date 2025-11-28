from abc import ABC, abstractmethod   #abtrst the  base class  
class Calc(ABC):
    @abstractmethod
    def operation(self):
        pass



class Add(Calc):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operation(self):
        return self.a + self.b

class Sub(Calc):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operation(self):
        return self.a - self.b


class Mul(Calc):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operation(self):
        return self.a * self.b

class Div(Calc):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def operation(self):
        return self.a // self.b       

obj = Add(6, 5)
obj2 = Sub(6, 5)
obj3= Div(6, 5)
obj4 = Mul(6, 5)
print( obj.operation())
print( obj2.operation())
print( obj3.operation())
print( obj4.operation())