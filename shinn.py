class Game:
    def __init__(self,name ,amount,date ):
        self.name = name 
        self._amount =amount
        self.__date = date

    def show(self):
        return f'Game name : {self.name}, Game amount:{self._amount}, Date: {self.__date}'
    
    def get_date(self):
        return f'Udate date :{self.__date}'
    
    def set_date(self,date):
        self.__date =date

obj = Game("GTA 6", 5000, "2025-01-01")

print(obj.show())          
print(obj.get_date())      
obj.set_date("2026-07-08") 
print(obj.get_date())       