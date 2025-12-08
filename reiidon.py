class Employeeee:
    company = "apple"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employeeee.company}")
    
    @classmethod 
    def comhh(cls,newcompany):
        cls.company=newcompany

    @staticmethod
    def salary(salary):
        return salary < 0
    
obj1 = Employeeee("riya", 30000)
obj2 = Employeeee("Sankeerth", 45000)
obj3 = Employeeee("shins", 50000)

obj1.show()
obj2.show()
obj3.show()

print(Employeeee.salary(20000))  