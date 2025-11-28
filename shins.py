class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def addition(self):
        result = self.x + self.y
        print( result)

    def mul (self):
        result = self.x * self.y
        print( result)

    def div(self):
        result = self.x // self.y
        print( result)

    def sub(self):
        result = self.x - self.y
        print( result)