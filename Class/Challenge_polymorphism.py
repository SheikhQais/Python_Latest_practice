def describe(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')
        
describe(name='Hania', Boy_Friend ='Asim Azhar',Age =10, Status=  'In-Relation')


# Polymorphism with Inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def move(self):
        print('Drives')
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def __init__(self):
        pass

    def move(self):
        print('Sails')
        
class Airplane(Vehicle):
    def __init__(self):
        pass
    
    def move(self):
        print('Flies')
        
car1 = Car('Honda','Civic')
boat = Boat()
plane = Airplane()

for x in [plane,car1,boat]:
    x.move()