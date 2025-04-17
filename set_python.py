#Set is the built-in data type of python, Which is unordered, unchangeable and unindexed
# And set items can be of any Data Type And a Set can contain different data types (int, string, boolean)
thisset = {"apple", "banana", "cherry", "apple", False, True, 0, 1}
print(thisset)
# Set does not allow duplication
d_set = {'apple', 'banana', 'orange', 'apple'}
print(d_set)

#To get the length of set
print(len(thisset)) #Output = 5, Apple is duplicate, True or False = 1 or 0

# Python's perspective, sets are defined as object with data type 'set'
print(type(thisset))

# set() constructor, can be used to make a set

that_set = set(('glasses', 'jeans', 'shirt')) #note the double round-brackets
print(that_set)

#You cannot access item in the set by refering to index. But you can use it by using loop,
# or ask it the specific value in the set with 'in' keyword

for x in thisset:
    print(x)
    
print('banana' in thisset, 'Yes') #output will be boolean
print('banana' not in thisset, 'No') #output will be boolean

if "watch" in that_set:
    print('Yes, it is.')
else:
    print("N/A")
    
# Once a set is created, it cannot be changed but you can add new item in it
thisset.add('Berry')
print(thisset)

#You can also add items from another set into a current set
thisset.update(that_set)
print(thisset)

#You can add any iterable(list, tuple, dictionary), it is not needed to be set only
this_list = [1,2,3,4,'get', 'on', 'the', 'dance', 'floor']
print(this_list)
thisset.update(this_list) #Check this
print(thisset)

#To remove item from set, you can use remove() or discard() method

thisset.remove('banana')
print(thisset)

# But if item is not available in the set, remove() method will throw thw error
# thisset.remove('stawberry')

#You can also use discard() method to remove the item from the set
thisset.discard('apple')
print(thisset)

#But if item is not available in the set, discard() method will not throw the error
thisset.discard('pent')
print(thisset)

#You can also remove the item with pop() method, but this method will remove the random item.
thisset.pop()
print(thisset) #sets are unordered, so do not know which item is going to be removed 

# clear() will empty the set
thisset.clear()
print(thisset)

#del keyword will delete the complete existance of the set
# del thisset
# print(thisset)

# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# union() method will return a new n=set with all items from both sets

set1 = {'Ali','hasan','hussain'}
set2 = {'Muhammad','Ali'}

set3 = set1.union(set2)
print(set3)

# You can also use '|' operator instead of union()
set3 = set1 | set2
print(set3) 

# Joining the multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

union_set = set1.union(set2,set3,set4)
print('Using union() method',union_set)

union_set = set1 | set2 | set3 | set4
print('using "|" operator',union_set)

# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Intersection
# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print('Using Intersection method',set3)

# You can use the '&' operator instead of the intersection() method

set3 = set1 & set2
print('Usimg "&" operator', set3)

#difference()
# The difference() method will return a new set that will contain only the items from the first set 
# that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print("Using difference() method",set3)
# You can also use the "-" operator instead of the difference() method
set3 = set1 - set2
print("Using'-' operator",set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print("Using difference_update() method",set1)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print("Using symmetric_difference() method",set3)

# You can also use "^" Operator instead of symmetric_difference() method
set3 = set1 ^ set2
print("Using '^' operator", set3)

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)