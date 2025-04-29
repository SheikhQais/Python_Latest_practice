class myClass:
    x = 5
    
p1 = myClass()
print(p1.x)

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:
# The __init__() function is called automatically every time the class is being used to create a new object.

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = person('Waleed',23)
print(p1.name,p1.age)