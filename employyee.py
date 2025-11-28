class Employee:
    company = "tech by liver "

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name, ", Salary:", self.salary, ", Company:", Employee.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0



obj1 = Employee("jishnu", 50000)
obj2 = Employee("sankeerth", 60000)
obj3 = Employee("vishal", 70000)

print(Employee.is_valid_salary(40000))  
print(Employee.is_valid_salary(-100))   


obj1.show_details()
obj2.show_details()
obj3.show_details()

Employee.change_company(" Tech by heart ")

obj1 = Employee("jishnu", 100000)
obj2 = Employee("sankeerth", 80000)
obj3 = Employee("vishal", 790000)


obj1.show_details()
obj2.show_details()
obj3.show_details()

