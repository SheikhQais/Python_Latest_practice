# Polymorphism mean "Many forms", it refers to methods/fucntions/operators with same names that can be 
# executed in many objects and classes e.g len() excutes differently in Strings, Tuple and Dictionary etc

stg = "Hello World!"
print(len(stg)) # print number of characters

tup = ('Hello', 'World', 'Baby!')
print(len(tup)) # print number of items

dic = {'make': 'Honda', 'Model': 'Civic', 'Varient': '1.8cc'}
print(len(dic)) # print number of key value pairs

#Polymorphism usually used in class methods, where we can have multiple classes with same method name.
#For example if we have different classes 'car', 'airplane' and 'boat' we can use move() method differently in all.

class car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def move(self):
        print('drives')
        
class boat: 
    def __init__(self, company):
        self.company = company
    
    def move(self):
        print('sails')
        
class airplane:
    def __init__(self, company):
        self.company = company
    
    def move(self):
        print('Flies')
        
car1 = car('honda','civic')
air = airplane('AirSial')
boat1 = boat('J&C')

for x in (car1,air,boat1):
    x.move()