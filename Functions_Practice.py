# Write a function greet_people that accepts any number of names and prints "Hello" to each person.
# Example:
# greet_people('Ali', 'Zara', 'Usman')
# Solution:
def greet_people(*people):
    for x in people:
        print(f"Hello {x}")

greet_people('Ali', 'Zara', 'Usman')