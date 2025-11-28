class Image:
    def __init__(self, name, age, marks):
        self.name = name
        self._age = age  
        self.__marks =marks

    def show(self):
        return f"name:{self.name},age:{self._age}"

obj = Image("sankkerr", 90,40)
print(obj.show())
print(obj.name)
print(obj._Image__marks)
