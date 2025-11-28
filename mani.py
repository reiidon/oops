class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Studentr(Student):
    def __init__(self, name, age, marks):
        super().__init__(name, age)   
        self.marks = marks
    
    def student_detail(self):
        return f"Student name: {self.name}, Student age: {self.age}, Student marks: {self.marks}"


obj = Studentr("shins", 20, 70)
print(obj.student_detail())
