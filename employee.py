class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_name(self):
        print("Name:",self.name)

    def get_salary(self):
        print("Salary:",self.salary)