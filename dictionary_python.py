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
           "Varient": "F150",
           "year":2021
           }
print(thisdic)
thisdic.pop("Make")
print(thisdic)

thisdic.update({"Make":"Ford"})
print(thisdic)

thisdic.popitem()
print(thisdic)
# del thisdic["year"]
# print(thisdic)
# thisdic.clear()
# print(thisdic)

# Looping through the dictionary
for x in thisdic:
  print(x)
print("------------------")
print("Using index, it will give values in dictionary")
for x in thisdic:
  print(thisdic[x])
print("------------------")
print("Using values() method")
for x in thisdic.values():
  print(x)
print("------------------")
print("Using keys() method")
for x in thisdic.keys():
  print(x)
print("------------------")
print("Using items() method")
for x, y in thisdic.items():
  print(x,y)
  
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

mydict = thisdic.copy()
print("mydict=",mydict)

# Another way to make a copy is to use the built-in function dict().

mydict = dict(thisdict)
print("mydict=",mydict)

# Nested Dictionaries

# A Dictionary can contain dictionaries, called nested dictionaries
Family = {
  "child1": {
    "name":"Qais",
    "age":24
  },
  "child2": {
    'name': "Abuzar",
    "age": 15
  },
  "child3": {
    'name': "Esha",
    "age": 22
  }
}

print("Family =",Family)

print(Family["child2"]["name"])

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

Child1 = {
  'name':'Habib',
  'age': 24
}

Child2 = {
  'name': 'Junaid',
  'age': 23
}

Child3 = {
  "name": "Abid",
  'age': 25
}

Colleages = {
  'Col1': Child1,
  'Col2': Child2,
  'Col3': Child3
}

print("Colleages =",Colleages)

# Looping through Nested Dictionary
for i, obj in Family.items():
  print(i)
  for y in obj:
    print(y,":",obj[y])