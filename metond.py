class Student:
    count =0
    def __init__(self,name ,age):
        self.name = name
        self.age = age
        Student.count += 1

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
    @classmethod
    def show_total_students(cls):
        print(f"Total Students: {cls.count}")

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return "Adult"
        else:
            return "Minor"
obj = Student ("shins", 20)
obj1 = Student ("jishnu ", 17)

obj.show_details()
Student.show_total_students()
print(Student.is_adult(16))
