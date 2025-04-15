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

print(list1[-3])
print(list1[-1])
print(list1[1:5])
print(list1[-5:])
print(list1[:6])

if "Cherry" in rup:
    print("Yes, Cherry is in the tupple")
else:
    print("No, It's not in the tupple")
    
#You cannot change the value in the tupple, But there is a workaround,
# you will convert tupple into list, make changes and then convert it back to tupple.

Tupple1 = ('Orange', 'Guava', 'Stawberry', 'Blue-Berry')
print("Before: ", Tupple1)
List2 = list(Tupple1)
List2[3]= 'Kiwi'
Tupple1 = tuple(List2)
print('After: ',Tupple1)

# Same, as Tupple is unchangeable or immuable, there is no append() built-in fuction to add item
# You will have to convert tuple into list and then add the item and convert back into tuple

Tupple2 = ('lelelmke', 'judshsd', 'kidjuhsdu','jjndsjnds')
print("Before: ",Tupple2)
list5 = list(Tupple2)
list5.append('Orange')
Tupple2 = tuple(list5)
print("After ",Tupple2)

#You can also add tuple with tuple: tuple1 + tuple2
# Make a new tuple (tuple2) with items to add in tuple and add it with tuple1

Tupple3 = (1,2,3,4,5,6)
print("Before: ",Tupple3)
Tupple4 = (8,9,8,7,7)
Tupple3 = Tupple3 + Tupple4
print("After: ",Tupple3)

# Tuples are unchangeable, so you cannot remove items from it,
# but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
print('Before: ', thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print('After: ', thistuple)

# Or you can delete the tuple completely:
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists


# Packing a tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print("Unpacking using * 'Asterisk'")
print(green)
print(yellow)
print(red, type(red)) 

print("If we use the Asterisk in the middle or starting item.")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(*green, tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Looping in the Tuple
print('Loops in the Tuple')
# For Loop
print('For Loop: ')
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
# While Loop
print('While Loop: ')
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1