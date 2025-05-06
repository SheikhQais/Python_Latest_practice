class car:
    def __init__(self, make, model, varient):
        self.make = make
        self.model = model
        self.varient = varient
        
    def __str__(self):
        return f'{self.make} {self.model} {self.varient}'
    
    def display_info(abc):
        return f'Make:{abc.make} Model:{abc.model} Varient:{abc.varient}'
        
car1 = car('Honda','Civic','X')
print(car1.display_info())
print(car1)

del car1.model #Deleting Object attribite 
# print(car1) #This will raise error, as class is already deleted

class student:
    def __init__(self, name, roll_number, grades):
        self.name = name
        self.roll_number = roll_number
        self.grades = grades
    
    def __str__(self):
        return f'{self.name} {self.roll_number} {self.grades}'
    
    def introduce(abc):
        print(f'Hi! My name is: {abc.name} and My Roll Number is: {abc.roll_number}')
        
    def average(abc):
        grades = 0
        x = 0
        while(x < len(abc.grades)):
             grades += abc.grades[x]
             x += 1
        grades = grades/len(abc.grades)
        print(f'My Average grades are {grades}')
        
    def calculate_gpa(self):
        pass
    
student1 = student('Qais','Bitf19M041',[65,66,76,55,86])

student1.introduce()
student1.average()
print(student1)

del car1 #Deleting Object
del student1 #Deleting Object

class book:
    def __init__(self, title, author,rating):
        self.title = title
        self.author = author
        
    def __str__(self):
        pass
    
    def book_info(abc):
        print(f'{abc.title} {abc.author}')
    
    def set_rating(abc, x):
        abc.rating = x
        return abc.rating
        
userr = book('bad to good days','Ans',5)
print(userr.rating) #This will raise error as rating is not initiated in __init__()
userr.set_rating(4.4) #So, We are assigning this attribute to the object of class in a method
print(userr.rating)