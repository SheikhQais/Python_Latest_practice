class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
    
    def sound(abc):
        print('Animal Speaks.')
        
class Dog(Animal):
    def __init__(self,name,specie):
        super().__init__(name, specie)
    
    def sound(abc):
        print(f'{abc.specie} sounds "Woof"')
        
class Cat(Animal):
    def __init__(self,name,specie):
        super().__init__(name, specie)
    
    def sound(abc):
        print(f'{abc.specie} sounds "Meow"')
        
d = Dog('Husky','Dog')
d.sound()

c = Cat('Kitty','Cat')
c.sound()