# Problem Statment:

# Filter Names by Length
# Create a list of names, then use list comprehension to create a new list containing only names with more than 4 characters.
# Example:
# names = ['Ali', 'Ahmed', 'Zara', 'Hassan', 'Noor']
# Expected output:
# ['Ahmed', 'Hassan']

names = ['Ali', 'Ahmed', 'Zara', 'Hassan', 'Noor']
filtered_list = [x for x in names if len(x) > 4]

print("Here is the filtered list: ")
print(filtered_list)