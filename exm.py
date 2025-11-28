class Calculator:
    def add(self, *args):
        return sum(args)

obj=Calculator()
print(obj.add(10, 20))




class Multiply:
    def mul(self, *numbe):
        result = 2 
        for num in numbe:
            result *= num
        return result


obj = Multiply()

print(obj.mul(5))       
print(obj.mul(5, 10))    
print(obj.mul(2, 3, 4))  
