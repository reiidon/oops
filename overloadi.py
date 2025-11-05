def addition(*args):
    total = sum(args)
    print( total)

addition(10, 20)
addition(5, 10, 15)
addition(1, 2, 3, 4, 5)


class Calculator:
    def add(self, *args):
        total = sum(args)#removing * and list the values [3,5]
        print( total)

obj=Calculator()
obj.add(10, 20)
obj.add(5, 10, 15)
obj.add(10,22,45,66)


