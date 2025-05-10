class person:
    def __init__(self,name):
        self.name = name
        
    def display(self):
        pass
    
class student(person):
    def __init__(self, name, roll_number, grades):
        super().__init__(name)
        self.roll_number = roll_number
        self.grades = grades
        
    def Average_Grades(self):
        Avg = int(sum(self.grades)/len(self.grades))
        print(f'Average Grades of {self.name} are: {Avg}')
        
    def display(self):
        print(f'Student\'s name: {self.name} \nRoll Number: {self.roll_number} \nGrades List: {self.grades}')
    
class teacher(person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def display(self):
        print(f'Teacher\'s name: {self.name} \nSubject: {self.subject}')
        
S1 = student('Azaan', 'BitF19m041', [78,98,99,67,77,56])
S1.Average_Grades()
S1.display()

T1 = teacher('Asif', 'Mathematics')
T1.display()