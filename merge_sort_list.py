# Problem Statement:
# Merge and Sort Two Lists
# Take two lists of strings, merge them, remove duplicates, and return a single alphabetically sorted list.
# Example:
# list1 = ['apple', 'banana', 'mango']
# list2 = ['banana', 'orange', 'grape']
# Expected output:
# ['apple', 'banana', 'grape', 'mango', 'orange']

list1 = ['apple', 'banana', 'mango']
list2 = ['banana', 'orange', 'grape']

merged_list = list1 + list2 # Merging boths list -> list1 and list2
print("here is the merged list"+str(merged_list))
merged_list = list(set(merged_list)) # Removing the duplicate by converting the list into set as set don't allow duplicate 
                                     # And again converting set into list
merged_list.sort()
print('After merging and sorting both lists')
print(merged_list)