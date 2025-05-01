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
    
# The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:
    def introduce(self):
        return f'Hello My name is: {self.name} and my age is: {self.age}'
    
    def callName(abc):
        return f'My name is {abc.name}'    
p1 = person('Waleed',23)
# print(p1.name,p1.age)

p2 = person('Qais',24)

print(p1)
print(p1.introduce())
print(p1.callName())

# You can modify properties on objects like this:
p1.age = 40
print(p1.age)

print(p2.introduce())
print(p2.age)

# You can delete properties on objects by using the del keyword:

del p1.age
# print(p1.age)

# You can delete objects by using the del keyword:

del p1
print(p1)

# The pass Statement
# class definitions cannot be empty, but if you for some reason have -
# a class definition with no content, put in the pass statement to avoid getting an error.
# Example
class mycar:
    def __init__(self,make,model,varient):
        pass
    
