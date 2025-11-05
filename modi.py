class Calculator:

    def __init__(self, x, y):  
        self.x = x             
        self.y = y
        
    def add(self):
        total = self.x + self.y
        print( total)
        
    def sub(self):
        total = self.x - self.y
        print(  total)

    def multi(self):
        total = self.x * self.y
        print( total)

    def div(self):
        total = self.x // self.y
        print( total)
         
        
