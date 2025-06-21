class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def Display(self):
        print(f"Name: {self.name} \nGrade: {self.grade}")
        
Std1 = Student('Ali', 90)
Std1.Display()