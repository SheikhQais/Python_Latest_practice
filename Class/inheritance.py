class person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  
  def __str__(self):
    return (f'Full Name: {self.firstname} {self.lastname}')
  
  def printName(abc):
    print(f'{abc.firstname}, {abc.lastname}')
    
p1 = person('Asjad', 'ALi')
p1.printName()
print(p1)

# Create a Child Class
# To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class

class student(person):
  pass

# Now the Student class has the same properties and methods as the Person class.
# Use the Student class to create an object, and then execute the printname method:

s1 = student('Ali','Ibrahim')
s1.printName()
print(s1)

# Add the __init__() Function

class student(person): #When you add the __init__() function, the child class will no longer inherit the parent's __init__() funct
  def __init__(self, fname, lname, year): #The child's __init__() function overrides the inheritance of the parent's __init__() function.
    self.firstname = fname
    self.lastname = lname
    self.Graduation_year = year
    
  def printStudent(abc):
    print(f'First Name is: {abc.firstname} \nLast Name is: {abc.lastname} \nGraduation Year: {abc.Graduation_year}')
    
s2 = student('Fajar','Nadeem',2023)
s2.printStudent()

# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.

class teacher(person):
  def __init__(self,namef,namel,subject):
    super().__init__(namef,namel)
    self.AssignedSubject = subject
    
  def welcome(abc):
    print(f'My name is {abc.firstname} {abc.lastname} And I\'ll be teaching you {abc.AssignedSubject}')
    
t1 = teacher('Zahid','Mehmood','Chemistry')
t1.welcome()