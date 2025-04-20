thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

# The values in dictionary items can be of any data type:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

print(type(thisdict))

thisdict = dict(name='Qais',age=25,Gender= 'Male')
print(thisdict)

x = thisdict["name"]
print(x)

print(thisdict["Gender"])
print(thisdict.get("Gender"))

y = thisdict.keys()
print(y)

z = thisdict.values()

thisdict["age"] = 20
print(z)

c = thisdict.items()
print(c)

thisdict["DOB"] = 2000  #Adding new item or key-value pair in dictionary
print(thisdict)

if "age" in thisdict: #Checking, If key is present in dictionary or not
  print("Yes, it is")
else:
  print("No, It's not")
  
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict.update({"age":27})
print(thisdict["age"])

# The update() method will update the dictionary with the items from a given argument. 
# If the item does not exist, the item will be added. The argument must be a dictionary, 
# or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

# Removing Items
# There are several methods to remove items from a dictionary:

thisdic = {"Make":"Ford",
           "Model": "Raptor",
           "Varient": "F150"
           }

thisdic.pop("Make")
print(thisdic)

thisdic.update({"Make":"Ford"})
print(thisdic)