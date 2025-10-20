# My_List = ['butter', 'chicken','bread', 'eggs', 'beef']
# print(My_List[:4])
# print(My_List)

# if "beef" in My_List:
#     print('yes! beef is in the list')
# else:
#     print('No, It\'s not in the list')
    
# My_List[1:3] =['Cheery','Mango'] 
# print(My_List)

# # thislist = ["apple", "banana", "cherry"]
# My_List[1:2] = ["blackcurrant", "watermelon"]
# print(My_List)
# print(len(My_List))

# # Adding the element in the range from 1 but 4 isn't included
# My_List[1:4] = ["black", "water"]
# print(My_List)

# # Insert() method will add the element in the given position and rest elements will move to next index in their position.
# My_List.insert(0,'plack')
# print(My_List)

# # append() method will ass the new element at the end of the list
# My_List.append('Fuckkkkkkk')
# print(My_List)

# # You can add any Iterable (Set,Dictionery,Tupple) in the list By this extend() method
# nd_List = ('Ohh','Yeah','Baby')
# My_List.extend(nd_List)
# print(My_List)

# # Removing the specific value item from the List
# My_List.remove('Baby')
# print(My_List)

# if 'Ohh' in My_List:
#     My_List.remove('Ohh')
# print(My_List)

# # pop() method will remove the specific index item
# My_List.pop(4)
# print(My_List)

# # If we don't specify the index, then pop() method will remove the last item of the list
# My_List.pop()
# print(My_List)

# # del keyword will also remove the specific index element from the list
# del My_List[1]
# print(My_List)

# # Clear() method will remove all the elements of list but List will exist, "No content in the List"
# My_List.clear()
# print(My_List)


ls = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

print(ls)

ls[1:3] = ['blackcurrant', 'watermelon']
print(ls)

if "orange" in ls:
    ls.remove('orange') #` removes the first occurrence of the value`
    ls.pop() # removes the last item if pop() is called without an index

print(ls)
ls.insert(2, 'grape')
print(ls)
ls.pop(1)
print(ls)

ls3 = ['pear', 'peach']
ls.extend(ls3)
print(ls)

del ls[4]
print(ls)

# ls.clear()
# print(ls)

for x in ls:
    print(x)

print("----Using while loop----")
i = 0
while i < len(ls):
    print(ls[i])
    i += 1

print("----Using List Comprehension----")

[print(x) for x in ls]  # List comprehension to print each item

for x in ls:
    for y in x:
        if 'o' in y:
            print(y, 'contains in', x)

print("----Sorting the list----")
ls.sort()
print(ls)

print("----Sorting the list in reverse order----")
ls.sort(reverse=True) #for descending order
print(ls)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)
for x in list2:
    list1.append(x)
print("----Merging two lists----")
print(list1)