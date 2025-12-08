class company:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        return f'name :{self.name}, salary{self.salary}'
class employee:
    def __init__(self, name, salary, language):
        super().__init__(name,salary)
        self.language = language

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}")

    
        

        
