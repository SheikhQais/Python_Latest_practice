# Write a function greet_people that accepts any number of names and prints "Hello" to each person.
# Example:
# greet_people('Ali', 'Zara', 'Usman')
# Solution:
def greet_people(*people):
    for x in people:
        print(f"Hello {x}")

greet_people('Ali', 'Zara', 'Usman')

# Create a function student_profile that accepts name, age, and city as keyword arguments (like name='Ali', etc.).
# Inside the function, print each key and value nicely formatted.

# Example Call:
# student_profile(name="Ali", age=21, city="Lahore")
print('\n')
def student_profile(**arg):
    for x, y in arg.items():
        print(f"{x} : {y}")
        
student_profile(name = 'Ali', age = 23, city = 'Lahore')

# Write a function called sum_marks that:
# Takes a list of marks as a parameter.
# Adds all the marks together.
# Returns the total sum.

# marks = [85, 90, 78, 92]
# sum_marks(marks)
# Expected Output:
# Total marks: 345
print('\n')

def sum_marks(marks):
    results = 0
    for x in range(len(marks)):
        results += marks[x]
        x += 1
    return results

marks = [85, 90, 78, 92]
print(sum_marks(marks))

