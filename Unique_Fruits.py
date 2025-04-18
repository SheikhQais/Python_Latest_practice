basket = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']

Fruits_Set = set(basket)
print(Fruits_Set)

for x in Fruits_Set:
    print(x.upper())

Fruits_Set.add("mango")
Fruits_Set.discard('grape')

print(Fruits_Set)