# Creating Tupple -> Ordered, Unchangeable and Allow Duplicate Value
tup = (1,2,3,4,5,6,7,8,9)
uup = (1) # single digit in the curly bracket is 'int' in Python, This isn't Tupple.
vup = (1,) # It's important to type ',' after single digit. This is tuple.
print(type(tup), tup)
print(type(uup), uup)
print(type(vup), vup)

rup =('Cherry', 'Banana', 'Mango', 'Orange', 'Banana') # Tupple allows duplicate values in it
print(len(rup),rup)