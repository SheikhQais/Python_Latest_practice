class myClass:
    x = 5
    
p1 = myClass()
print(p1.x)

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:
# The __init__() function is called automatically every time the class is being used to create a new object.

#The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):                      
        return f'{self.name} {self.age}'
p1 = person('Waleed',23)
# print(p1.name,p1.age)

print(p1)