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

that_set = set(('watch','glasses', 'jeans', 'shirt'))
print(that_set)