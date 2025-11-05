class Parent:
    def find(self):
        print("shins")

class Child(Parent):   
    def find(self):
        print("hello")

d = Child()
d.find()
s = Parent()
d.find()  

