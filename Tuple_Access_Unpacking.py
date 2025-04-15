person = ('Ali', 25, 'Lahore')
for x in person:
    if x == "Lahore":
        print(x, person.index(x))
(name, age, city) = person
print(name)
print(age)
print(city)