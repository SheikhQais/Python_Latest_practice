My_List = ['butter', 'chicken','bread', 'eggs', 'beef']
print(My_List[:4])
print(My_List)

if "beef" in My_List:
    print('yes! beef is in the list')
else:
    print('No, It\'s not in the list')
    
My_List[1:3] =['Cheery','Mango'] 
print(My_List)

# thislist = ["apple", "banana", "cherry"]
My_List[1:2] = ["blackcurrant", "watermelon"]
print(My_List)
print(len(My_List))

# Adding the element in the range from 1 but 4 isn't included
My_List[1:4] = ["black", "water"]
print(My_List)

# Insert() method will add the element in the given position and rest elements will move to next index in their position.
My_List.insert(0,'plack')
print(My_List)

# append() method will ass the new element at the end of the list
My_List.append('Fuckkkkkkk')
print(My_List)

# You can add any Iterable (Set,Dictionery,Tupple) in the list By this extend() method
nd_List = ('Ohh','Yeah','Baby')
My_List.extend(nd_List)
print(My_List)

# Removing the specific value item from the List
My_List.remove('Baby')
print(My_List)

if 'Ohh' in My_List:
    My_List.remove('Ohh')
print(My_List)

# pop() method will remove the specific index item
My_List.pop(4)
print(My_List)

# If we don't specify the index, then pop() method will remove the last item of the list
My_List.pop()
print(My_List)

# del keyword will also remove the specific index element from the list
del My_List[1]
print(My_List)

# Clear() method will remove all the elements of list but List will exist, "No content in the List"
My_List.clear()
print(My_List)

# If we don't give index of item, del keyword will delete the complete List
del My_List
print(My_List)