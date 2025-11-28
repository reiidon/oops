class Bankk:
    def __init__(self,name ,account_number,balance):
        self.name =name
        self._account_number = account_number
        self.__balance = balance

    def show(self):
        return f"name:{self.name},account_number:{self._account_number}, self.__balance :{self.__balance}"
obj = Bankk("shins",20071528111,2000)
print(obj.show())
print(obj.name)
print(obj._account_number)
print(obj._Bankk__balance)
obj.name ="shins"
obj._Bankk__balance = 4000
print(obj.show())
