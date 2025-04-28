# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

# Use the len() method to return the length of an array (the number of elements in an array).
x = len(cars)
print(x)

# You can use the for in loop to loop through all the elements of an array.
for x in cars:
  print(x)
  
# You can use the append() method to add an element to an array.
cars.append("Honda")

# You can use the pop() method to remove an element from the array.
# Delete the second element of the cars array:
cars.pop(1)

# You can also use the remove() method to remove an element from the array.
# Delete the element that has the value "Volvo":
cars.remove("Volvo")