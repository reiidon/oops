class Car:

    count = 0
     
    def __init__(self,name , date ):
        self.name= name
        self.date=date
        Car.count+=1

    def show(self):
        return f'Car name :{self.name} , Car launge is : {self.date}'
    @classmethod

    def show_nn(cls):
        return f'Car count : {cls.count}'
    
    @staticmethod
    def number(num):
        return f'numer is :{num}'
    
obj = Car ("bmw",2243)
obj1 = Car ("benz",2381)
print(obj.show())

print(Car.show_nn())
