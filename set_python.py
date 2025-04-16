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
del thisset
print(thisset)