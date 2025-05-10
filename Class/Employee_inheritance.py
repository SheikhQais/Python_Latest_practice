class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def display(abs):
        pass
    
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
        
    def display(abs):
        print(f'Name: {abs.name}, Salary: {abs.salary}, Department: {abs.department}')
        
Emp = Manager('Murshad', 80000, 'IT')
Emp.display()