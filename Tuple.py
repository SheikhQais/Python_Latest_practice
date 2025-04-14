# Creating Tupple -> Ordered, Unchangeable and Allow Duplicate Value
tup = (1,2,3,4,5,6,7,8,9)
uup = (1) # single digit in the curly bracket is 'int' in Python, This isn't Tupple.
vup = (1,) # It's important to type ',' after single digit. This is tuple.
print(type(tup), tup)
print(type(uup), uup)
print(type(vup), vup)

rup =('Cherry', 'Banana', 'Mango', 'Orange', 'Banana') # Tupple allows duplicate values in it
print(len(rup),rup)

#tupple items cqan be of any data type
tuple1 = ("abc", 34, True, 40, "male")
print(len(tuple1), tuple1)

#You can use Tupple constructor tupple(), Here I changed a list into tupple
list1 = [2,3,4,5,6,7,7]
print(type(list1), list1)

list1 = tuple(list1)
print(type(list1), list1)

#Accessing Tupple Item
print(list1[3], type(list1))